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

#  [Logger](Logger.html).LogWarning

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

public void LogWarning(string tag, object message);

## Declaration

public void LogWarning(string tag, object message, [Object](Object.html)
context);

### Parameters

tag | Used to identify the source of a log message. It usually identifies the class where the log call occurs.  
---|---  
message | String or object to be converted to string representation for display.  
context | Object to which the message applies.  
  
### Description

A variant of [Logger.Log](Logger.Log.html) that logs an warning message.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private static [ILogger](ILogger.html) logger = [Debug.unityLogger](Debug-unityLogger.html);
        private static string kTAG = "MyGameTag";
        private [Transform](Transform.html) tr;  
      
        void MyGameMethod()
        {
            if (tr == null)
            {
                logger.LogWarning(kTAG, "memberVariable must be set to point to a [Transform](Transform.html).", tr);  
      
                Debug.unityLogger.LogWarning(kTAG, "Failed! to set [Transform](Transform.html)",  tr);
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

