# Salt and Sanctuary Archipelago Setup Guide

## Requirements

- **Salt and Sanctuary** (PC, Steam version)
- **Flips** (Floating IPS patcher) — [download here](https://github.com/Alcaro/Flips/releases)
- **Salt and Sanctuary AP Patch** (`.bps` file) — included with your Archipelago installation
- **Archipelago** 0.6.6 or later — [archipelago.gg](https://archipelago.gg)

---

## Step 1: Back Up Your Game Executable

> ⚠️ **This step is mandatory. Do not skip it.**
>
> The patch permanently modifies `salt.exe`. If you do not keep a backup you will need to verify your game files through Steam to restore the original.

1. Navigate to your Salt and Sanctuary install folder. The default location is:
   ```
   C:\Program Files (x86)\Steam\steamapps\common\Salt and Sanctuary\
   ```
2. Find `salt.exe`.
3. Make a copy of it **in the same folder** and rename the copy to `salt-backup.exe`.

Your folder should now contain **both** files:
```
salt.exe          ← this is what gets patched
salt-backup.exe   ← your untouched original, keep this safe
```

If you ever need to restore the original (e.g. to play unmodded or update the game), delete `salt.exe` and rename `salt-backup.exe` back to `salt.exe`.

---

## Step 2: Patch the Executable with Flips

1. Open **Flips**.
2. Click **Apply Patch**.
3. When prompted for the patch file, select the **Salt and Sanctuary AP patch** (`.bps` file).
4. When prompted for the file to patch, navigate to your install folder and select **`salt.exe`**.
5. When prompted for the output file, save it as **`salt.exe`** in the same folder (overwriting the original — you already backed it up in Step 1).

Flips will confirm the patch was applied successfully. If it reports a checksum error, make sure you are patching the **original unmodified** `salt.exe` and not a previously patched version. Restore from `salt-backup.exe` and try again.

---

## Step 3: Install the APWorld

1. Locate the `salt_and_sanctuary.apworld` file.
2. Double-click it — Archipelago will install it automatically. Alternatively, copy it manually to:
   ```
   %appdata%\Archipelago\custom_worlds\
   ```
3. Restart the Archipelago Launcher if it was already open.

> ⚠️ **Remove any older versions of the Salt and Sanctuary APWorld before installing.** Having two APWorlds that register the same game name will cause a startup error. Check both:
> ```
> %appdata%\Archipelago\custom_worlds\
> C:\ProgramData\Archipelago\lib\worlds\
> ```

---

## Step 4: Generate a Multiworld

1. Create your YAML options file. A template is available in the Archipelago Launcher under **Generate Template Options**.
2. Place your YAML in the Archipelago `Players` folder.
3. Run generation via the Archipelago Launcher or web host.

---

## Step 5: Connect to Archipelago In-Game

1. Launch the patched `salt.exe`.
2. Start or load a save file.
3. The Archipelago connection is done through a text file called archipelago.txt. This is located in Salt and Sanctuary game folder usually in documents or the like. Saves are kept here as well.
4. Enter your **server address**, **slot name**, and **password** (if any).
5. Save the file and open the game. The client will confirm when it is connected and your slot is found by showing AP Connected in green at the top of your screen or red if it didn't work. This won't appear UNTIL YOU ARE IN GAME!

> If the game cannot connect, check that your server address includes the port (e.g. `archipelago.gg:12345`) and that your slot name exactly matches the one used during generation.

---

## Updating the Patch

When a new version of the APWorld or patch is released:

1. Restore your original exe: delete `salt.exe`, rename `salt-backup.exe` to `salt.exe`.
2. Re-apply the new `.bps` patch following Step 2.
3. Install the new `.apworld` following Step 3.

Do not patch an already-patched exe. Always patch from the clean backup.

---

## Troubleshooting

**"Game Salt and Sanctuary already registered" error on generation**
You have two APWorlds installed. Remove all copies and reinstall just one. See Step 3.

**Flips reports a checksum mismatch**
You are trying to patch a file that has already been patched, or the wrong file. Restore `salt-backup.exe` to `salt.exe` and try again.

**Client connects but checks are not sending**
Verify the APWorld version used to generate the room matches the installed APWorld. Regenerate if in doubt — item and location IDs must match exactly between the APWorld and the client mod.

**Options listed in my YAML are reported as invalid**
An outdated APWorld is installed and won the registration. Remove it and reinstall the correct version.
