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

#  [Component](Component.html).BroadcastMessage

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

public void BroadcastMessage(string methodName, object parameter = null,
[SendMessageOptions](SendMessageOptions.html) options =
SendMessageOptions.RequireReceiver);

## Declaration

public void BroadcastMessage(string methodName,
[SendMessageOptions](SendMessageOptions.html) options);

### Parameters

methodName | Name of the method to call.  
---|---  
parameter | Optional parameter to pass to the method (can be any value).  
options | Should an error be raised if the method does not exist for a given target object?  
  
### Description

Calls the method named `methodName` on every
[MonoBehaviour](MonoBehaviour.html) in this game object or any of its
children.

The receiving method can choose to ignore `parameter` by having zero
arguments. if options is set to
[SendMessageOptions.RequireReceiver](SendMessageOptions.RequireReceiver.html)
an error is printed when the message is not picked up by any component.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            /// Calls the function ApplyDamage with a value of 5
            BroadcastMessage("ApplyDamage", 5.0);
        }  
      
        // Every script attached to the game object and all its children
        // that has a ApplyDamage function will be called.
        void ApplyDamage(float damage)
        {
            print(damage);
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

