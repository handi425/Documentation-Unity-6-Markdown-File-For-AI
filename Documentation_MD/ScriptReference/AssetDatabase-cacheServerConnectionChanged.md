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

#  [AssetDatabase](AssetDatabase.html).cacheServerConnectionChanged

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

### Parameters

value | Use [CacheServerConnectionChangedParameters](CacheServerConnectionChangedParameters.html) for this event.  
---|---  
  
### Description

Unity raises this event when Cache Server connection is changed.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CacheServerConnectionChangedExample
    {
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Correct connection to the [Cache](Cache.html) Server")]
        static void CorrectChangeCacheServer()
        {
            var correctEndpoint = "192.168.1.210:8080";
            [EditorSettings.cacheServerEndpoint](EditorSettings-cacheServerEndpoint.html) = correctEndpoint;
            [AssetDatabase.RefreshSettings](AssetDatabase.RefreshSettings.html)();
        }  
      
        [[MenuItem](MenuItem.html)("[AssetDatabase](AssetDatabase.html)/Wrong connection to the [Cache](Cache.html) Server")]
        static void WrongChangeCacheServer()
        {
            var invalidEndpoint = "Invalid IP Address";
            [EditorSettings.cacheServerEndpoint](EditorSettings-cacheServerEndpoint.html) = invalidEndpoint;
            [AssetDatabase.RefreshSettings](AssetDatabase.RefreshSettings.html)();
        }  
      
        [InitializeOnLoadMethod]
        static void OncacheServerConnectionChanged()
        {
            [AssetDatabase.cacheServerConnectionChanged](AssetDatabase-cacheServerConnectionChanged.html) += ConsoleLog;
        }  
      
        static void ConsoleLog([CacheServerConnectionChangedParameters](CacheServerConnectionChangedParameters.html) param)
        {
            [Debug.Log](Debug.Log.html)("Connection Changed");
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

