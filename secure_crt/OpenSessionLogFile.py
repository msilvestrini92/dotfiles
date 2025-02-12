# $language = "python"
# $interface = "1.0"

# OpenSessionLogFile.py
#   Last Modified: 17 Oct, 2022
#     - Adjust code to work with either Python 2 or Python 3
#
#   Last Modified: 10 Apr, 2019
#     - Add support for /select argument to the script. If present,
#       the log file itself will not be opened; instead, Windows
#       Explorer will be opened, with the log file selected.
#
#   Last Modified: 21 Nov, 2012
#     - Initial revision
#
# Description
#   This script opens the log file associated with a current session's
#   configuration settings.  The session must have a log file name
#   configured in session options in order for this to operate successfully.
#
#   Also, if logging isn't currently enabled and the log file name contains
#   % substitutions for time and date, it may not be possible to determine
#   the actual log file to open.
#
#   However, in the 80% case, this script can be helpful in quickly opening
#   the configured log file path for the currently-active, logging session.

import SecureCRT
import subprocess, os, sys, platform

MsgBox = crt.Dialog.MessageBox
Prompt = crt.Dialog.Prompt

g_strDlgTitle = "Open Session's Log File"

def main():

    # Attempt to read the current log file name from session options
    strLogFileName = crt.Session.LogFileName.strip()

    if not crt.Session.Logging == True:

        if not strLogFileName == "":
            if not MsgBox(
                "This session isn't currently logging!\r\n\r\n"
                "Do you wish to open the log file configured in "
                "session options (if any)?",
                g_strDlgTitle,
                BUTTON_YESNO) == IDYES:
                return
        else:
            MsgBox(
                "There is no log file name defined in session "
                "options.\r\n\r\n"
                "This script requires a session configuration "
                "that defines a log file path.\r\n\r\n"
                "Make sure that you have a log file name defined in "
                "'Options / Session Options, Terminal / Log File'"
                "category.")
            return

    strSavedLogFileName = crt.Session.Config.GetOption("Log Filename")

    if strLogFileName == "":
        MsgBox(
            "No log file is configured for this session!",
            g_strDlgTitle)
        return

    bFileExists = os.path.isfile(strLogFileName)

    # Determine if there are any % substitutions in the log file name.
    # If so, we can't reliably determine the log file name because we
    # don't know if we have the information available to make the
    # necessary substitutions to get at the real log file name.
    if "%" in strSavedLogFileName:
        # Check to see if the file exists using the strLogFileName, which
        # will have substitutions made for us.  If the log file doesn't
        # exist, it means that there are time substitutions that prevent
        # us from getting at the real name of the log file (that we were
        # logging to earlier)
        if not bFileExists:
            MsgBox(
                "Configured log file contains substitutions:\r\n\r\n" +
                strSavedLogFileName + "\r\n\r\n" +
                "When a log file name contains substitutions (e.g. time) " +
                "it may be impossible to determine the log file name if " +
                "logging is not currently enabled.",
                g_strDlgTitle)
            return

    else:
        if not bFileExists:
            MsgBox(
                "Log file does not exist! \r\n\r\n%s" % strLogFileName)
            return

    OpenLogFile(strLogFileName)


def OpenLogFile(strFile):
    bSelectFileInsteadOfOpen = False
    if crt.Arguments.Count > 0:
        strArg = crt.Arguments.GetArg(0)
        strArg = strArg.lower()
        if strArg == "/select":
            bSelectFileInsteadOfOpen = True
    try:
        # subprocess.run(strFile)
        if os.name == "nt":
            if bSelectFileInsteadOfOpen:
                os.system("C:\\Windows\\Explorer.exe /e,/select,\"{0}\"".format(strFile))
            else:
                os.startfile(strFile)
        elif os.name == "posix":
            strOSVariant = str(os.uname()[0])
            # Handle opening of the file/browser on supported Linux platforms:
            if strOSVariant == "Linux":
                if bSelectFileInsteadOfOpen:
                    os.system(('nautilus -s "{0}"&'.format(strFile)))
                else:
                    subprocess.call(('xdg-open', strFile))
            # Handle opening of the file/browser on supported macOS platforms:
            elif strOSVariant == "Darwin":
                if bSelectFileInsteadOfOpen:
                    # This is how you select a file in Finder app on macOS:
                    os.system("open -R \"{0}\"".format(strFile))
                else:
                    subprocess.call(('open', strFile))
            else:
                MsgBox("Unsupported OS Variant: " + strOSVariant)
        else:
            MsgBox("Unsupported OS name: " + os.name)

    except Exception as objErr:
        MsgBox(
            "Failed to open \"" + strFile + "\" with the default app.\r\n\r\n"  +
            str(objErr).replace('\\\\', '\\').replace('u\'', '\''))


main()
