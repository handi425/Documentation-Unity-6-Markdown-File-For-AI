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

#  [AssetDatabase](AssetDatabase.html).GetCacheServerPort

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

public static ushort GetCacheServerPort();

### Returns

**ushort** Returns the Port number of the Cache Server in Editor Settings.
Returns 0 if Port number is not set in Editor Settings.

### Description

Gets the Port number of the Cache Server in Editor Settings.

Note: If you set a new value for the Port number, your new settings are not
applied until you call AssetDatabase.RefreshSettings(). However, this method
will return the value you have set regardless of whether you have applied the
setting or no.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class AssetDatabaseExamples : [MonoBehaviour](MonoBehaviour.html)  
      
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Debugging Connection to the [Cache](Cache.html) Server")]
        static void DebuggingConnectionToTheCacheServer()
        {
            //This will Enable [Cache](Cache.html) Server in Project [Settings](CameraEditor.Settings.html)
            [EditorSettings.cacheServerMode](EditorSettings-cacheServerMode.html) = [CacheServerMode.Enabled](CacheServerMode.Enabled.html);
            [Debug.Log](Debug.Log.html)("Is [Cache](Cache.html) Server Enabled? - " + [AssetDatabase.IsCacheServerEnabled](AssetDatabase.IsCacheServerEnabled.html)());  
      
            var cacheServerIP = "10.37.44.195";
            ushort cacheServerPort = 10443;  
      
            if ([AssetDatabase.IsConnectedToCacheServer](AssetDatabase.IsConnectedToCacheServer.html)() == false)
            {
                if ([AssetDatabase.CanConnectToCacheServer](AssetDatabase.CanConnectToCacheServer.html)(cacheServerIP, cacheServerPort) == false)
                {
                    [Debug.Log](Debug.Log.html)("[Cache](Cache.html) server is not available, check IP address and [Port](Experimental.GraphView.Port.html) Number");
                }  
      
                else
                {
                    [Debug.Log](Debug.Log.html)("[Cache](Cache.html) server is available, but not connected now. Set correct IP and [Port](Experimental.GraphView.Port.html) Number in Project [Settings](CameraEditor.Settings.html)");
                }
            }  
      
            else
            {
                [Debug.Log](Debug.Log.html)("[Cache](Cache.html) Server is connected");
                [Debug.Log](Debug.Log.html)("[Cache](Cache.html) Server IP: " + [AssetDatabase.GetCacheServerAddress](AssetDatabase.GetCacheServerAddress.html)());
                [Debug.Log](Debug.Log.html)("[Cache](Cache.html) Server [Port](Experimental.GraphView.Port.html) Number: " + [AssetDatabase.GetCacheServerPort](AssetDatabase.GetCacheServerPort.html)());
            }
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

