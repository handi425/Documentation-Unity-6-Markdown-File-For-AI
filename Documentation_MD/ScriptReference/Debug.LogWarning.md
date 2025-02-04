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

#  [Debug](Debug.html).LogWarning

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

[Switch to Manual](../Manual/class-Debug.html "Go to Debug Component in the
Manual")

## Declaration

public static void LogWarning(object message);

## Declaration

public static void LogWarning(object message, [Object](Object.html) context);

### Parameters

message | String or object to be converted to string representation for display.  
---|---  
context | Object to which the message applies.  
  
### Description

A variant of Debug.Log that logs a warning message to the console.

When you select the message in the console a connection to the context object
will be drawn. This is very useful if you want know on which object a warning
occurs.  
  
When the message is a string, rich text markup can be used to add emphasis.
See the manual page about [rich text](../Manual/StyledText.html) for details
of the different markup tags available.  
  
Additional resources: [Debug.unityLogger](Debug-unityLogger.html),
[ILogger](ILogger.html), [Logger.LogWarning](Logger.LogWarning.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class MyGameClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Transform](Transform.html) transform;  
      
        void MyGameMethod()
        {
            if (transform == null)
                [Debug.LogWarning](Debug.LogWarning.html)("A warning assigned to this transform!", transform);
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

