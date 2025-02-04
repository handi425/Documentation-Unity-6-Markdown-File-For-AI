[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Application](Application.html).persistentDataPath

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public static string persistentDataPath;

### Description

Contains the path to a persistent data directory (Read-only).

This value is a directory path where you can store data that you want to
retain between runs. When you publish on iOS and Android, `persistentDataPath`
points to a public directory on the device. The files can only be erased by
users directly and not by any app updates. **Note:** The difference slashes
indicate the different operating systems according to
Path.DirectorySeparatorChar.  
  
When you build the Unity application, a GUID is generated that is based on the
Bundle Identifier. This GUID is part of `persistentDataPath`. If you keep the
same Bundle Identifier in future versions, the application keeps accessing the
same location on every update.  
  
**UWP Apps** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to `C:\Users\<user>\AppData\LocalLow\<company
name>`.  
  
**Windows Editor and Windows Player** :
[Application.persistentDataPath](Application-persistentDataPath.html) usually
points to `%userprofile%\AppData\LocalLow\<companyname>\<productname>`. It is
resolved by [SHGetKnownFolderPath](https://docs.microsoft.com/en-
us/windows/win32/api/shlobj_core/nf-shlobj_core-shgetknownfolderpath) with
FOLDERID_LocalAppDataLow, or [SHGetFolderPathW](https://docs.microsoft.com/en-
us/windows/win32/api/shlobj_core/nf-shlobj_core-shgetfolderpathw) with
CSIDL_LOCAL_APPDATA if the former is not available.  
  
**WebGL** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to `/idbfs/<md5 hash of data path>` where the
data path is the URL stripped of everything including and after the last '/'
before any '?' components.  
  
**Linux** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to `$XDG_CONFIG_HOME/unity3d` or
`$HOME/.config/unity3d`.  
  
**iOS** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to
`/var/mobile/Containers/Data/Application/<guid>/Documents`.  
  
**tvOS** : [Application.persistentDataPath](Application-
persistentDataPath.html) is not supported and returns an empty string.  
  
**Android** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to
`/storage/emulated/<userid>/Android/data/<packagename>/files` on most devices
(some older phones might point to location on SD card if present), the path is
resolved using
[android.content.Context.getExternalFilesDir](https://developer.android.com/reference/android/content/Context#getExternalFilesDir\(java.lang.String\)).  
  
**Mac** : [Application.persistentDataPath](Application-
persistentDataPath.html) points to the user Library folder (This folder is
often hidden). In recent Unity releases, user data is written into
`~/Library/Application Support/company name/product name`. Older versions of
Unity wrote into the `~/Library/Caches` folder, or `~/Library/Application
Support/unity.company name.product name`. These folders are all searched for
by Unity. The application finds and uses the oldest folder with the required
data on your system.

    
    
    using UnityEngine;  
      
    public class Info : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Debug.Log](Debug.Log.html)([Application.persistentDataPath](Application-persistentDataPath.html));
        }
    }
    

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

