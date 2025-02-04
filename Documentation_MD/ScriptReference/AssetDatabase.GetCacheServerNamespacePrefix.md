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

#  [AssetDatabase](AssetDatabase.html).GetCacheServerNamespacePrefix

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

## Declaration

public static string GetCacheServerNamespacePrefix();

### Returns

**string** Returns the Namespace prefix for the Cache Server.

### Description

Gets the Cache Server Namespace prefix set in Editor Settings.

Note: If you set a new value for the Namespace prefix your new settings are
not applied until you call AssetDatabase.RefreshSettings(). However, this
method will return the value you have set regardless of whether you have
applied the setting or no.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)  
      
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Set [Cache](Cache.html) Server Project [Settings](CameraEditor.Settings.html)")]
        static void SetCacheServerProjectSettings()
        {
            [EditorSettings.cacheServerMode](EditorSettings-cacheServerMode.html) = [CacheServerMode.Enabled](CacheServerMode.Enabled.html);
            [Debug.Log](Debug.Log.html)("Is [Cache](Cache.html) Server enabled? - " + [AssetDatabase.IsCacheServerEnabled](AssetDatabase.IsCacheServerEnabled.html)());  
      
            [EditorSettings.cacheServerEndpoint](EditorSettings-cacheServerEndpoint.html) = "192.168.31.210:10443";
            [Debug.Log](Debug.Log.html)("[Cache](Cache.html) Server IP and [Port](Experimental.GraphView.Port.html) number: " + [AssetDatabase.GetCacheServerAddress](AssetDatabase.GetCacheServerAddress.html)() + ":" + [AssetDatabase.GetCacheServerPort](AssetDatabase.GetCacheServerPort.html)());  
      
            [EditorSettings.cacheServerEnableAuth](EditorSettings-cacheServerEnableAuth.html) = false;
            [EditorSettings.cacheServerEnableTls](EditorSettings-cacheServerEnableTls.html) = false;  
      
            [EditorSettings.cacheServerEnableDownload](EditorSettings-cacheServerEnableDownload.html) = true;
            [Debug.Log](Debug.Log.html)("Is [Cache](Cache.html) Server download enabled? - " + [AssetDatabase.GetCacheServerEnableDownload](AssetDatabase.GetCacheServerEnableDownload.html)());  
      
            [EditorSettings.cacheServerEnableUpload](EditorSettings-cacheServerEnableUpload.html) = true;
            [Debug.Log](Debug.Log.html)("Is [Cache](Cache.html) Server upload enabled? - " + [AssetDatabase.GetCacheServerEnableUpload](AssetDatabase.GetCacheServerEnableUpload.html)());  
      
            [EditorSettings.cacheServerNamespacePrefix](EditorSettings-cacheServerNamespacePrefix.html) = "default";
            [Debug.Log](Debug.Log.html)("[Cache](Cache.html) Server Namespace prefix: " + [AssetDatabase.GetCacheServerNamespacePrefix](AssetDatabase.GetCacheServerNamespacePrefix.html)());  
      
            //This command is required to apply changes to some of the [EditorSettings](EditorSettings.html) properties above
            [AssetDatabase.RefreshSettings](AssetDatabase.RefreshSettings.html)();
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

