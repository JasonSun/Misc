#pragma  once

/*
-----------------Export Functions--------------
*/

BOOL  __stdcall XLInitDownloadEngine();

DWORD __stdcall XLURLDownloadToFile(LPCTSTR pszFileName, LPCTSTR pszUrl, LPCTSTR pszRefUrl, LONG & lTaskId);

DWORD __stdcall XLQueryTaskInfo(LONG lTaskId, LONG *plStatus, ULONGLONG *pullFileSize, ULONGLONG *pullRecvSize);

DWORD __stdcall XLPauseTask(LONG lTaskId, LONG & lNewTaskId);

DWORD __stdcall XLContinueTask(LONG lTaskId);

DWORD __stdcall XLContinueTaskFromTdFile(LPCTSTR pszTdFileFullPath, LONG & lTaskId);

VOID  __stdcall XLStopTask(LONG lTaskId);

BOOL  __stdcall XLUninitDownloadEngine();

DWORD __stdcall XLGetErrorMsg(DWORD dwErrorId, LPTSTR pszBuffer, DWORD & dwSize);


/*
----------------------Task Status Define-----------------
*/
enum enumTaskStatus{
	enumTaskStatus_Connect = 0,                 // Set up connection
	enumTaskStatus_Download = 2,                // Start download
	enumTaskStatus_Pause = 10,                  // Pause
	enumTaskStatus_Success = 11,                // Download successfully
	enumTaskStatus_Fail = 12,                   // Download fail
};
