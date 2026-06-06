#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SKILL_NAME = "final-exam-course-rebuilder";
const EXCLUDES = new Set([
  ".git",
  ".gitignore",
  ".DS_Store",
  "node_modules",
  "package-lock.json",
  ".npmrc",
  "bin/final-exam-course-rebuilder-skill.js",
]);

function codexHome() {
  return process.env.CODEX_HOME || path.join(os.homedir(), ".codex");
}

function normalizeArgName(args, names) {
  return args.find((arg) => names.includes(arg));
}

function printUsage() {
  console.log(
    [
      "Usage:",
      "  final-exam-course-rebuilder-skill install [--skip-warn]",
      "  final-exam-course-rebuilder-skill uninstall",
      "  final-exam-course-rebuilder-skill path",
      "  final-exam-course-rebuilder-skill help",
      "",
      "Examples:",
      "  npx final-exam-course-rebuilder-skill install",
      "  npx final-exam-course-rebuilder-skill path",
      "  npx final-exam-course-rebuilder-skill uninstall",
    ].join("\n")
  );
}

async function copyDirectory(srcDir, destDir) {
  await fs.mkdir(destDir, { recursive: true });
  const entries = await fs.readdir(srcDir, { withFileTypes: true });

  for (const entry of entries) {
    if (EXCLUDES.has(entry.name)) continue;

    const srcPath = path.join(srcDir, entry.name);
    const destPath = path.join(destDir, entry.name);

    if (entry.isDirectory()) {
      if (entry.name === ".git") continue;
      await copyDirectory(srcPath, destPath);
      continue;
    }

    await fs.copyFile(srcPath, destPath);
  }
}

async function installSkill() {
  const sourceRoot = path.resolve(__dirname, "..");
  const targetRoot = path.join(codexHome(), "skills", SKILL_NAME);

  await fs.rm(targetRoot, { recursive: true, force: true });
  await copyDirectory(sourceRoot, targetRoot);
  console.log(`\nInstalled skill to: ${targetRoot}`);
  console.log("Restart Codex once to load the new/updated skill.");
}

async function uninstallSkill() {
  const targetRoot = path.join(codexHome(), "skills", SKILL_NAME);
  await fs.rm(targetRoot, { recursive: true, force: true });
  console.log(`Removed skill from: ${targetRoot}`);
  console.log("Restart Codex once to refresh installed skills.");
}

function showPath() {
  const targetRoot = path.join(codexHome(), "skills", SKILL_NAME);
  console.log(targetRoot);
}

async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0 || normalizeArgName(args, ["-h", "--help", "help"])) {
    printUsage();
    return;
  }

  const command = args[0];

  if (command === "install") {
    await installSkill();
    return;
  }

  if (command === "uninstall") {
    await uninstallSkill();
    return;
  }

  if (command === "path") {
    showPath();
    return;
  }

  printUsage();
}

main().catch((error) => {
  console.error(`Error: ${error.message}`);
  process.exit(1);
});
