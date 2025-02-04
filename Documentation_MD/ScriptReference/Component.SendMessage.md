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

#  [Component](Component.html).SendMessage

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

public void SendMessage(string methodName);

## Declaration

public void SendMessage(string methodName, object value);

## Declaration

public void SendMessage(string methodName, object value,
[SendMessageOptions](SendMessageOptions.html) options);

## Declaration

public void SendMessage(string methodName,
[SendMessageOptions](SendMessageOptions.html) options);

### Parameters

methodName | Name of the method to call.  
---|---  
value | Optional parameter for the method.  
options | Should an error be raised if the target object doesn't implement the method for the message?  
  
### Description

Calls the method named `methodName` on every
[MonoBehaviour](MonoBehaviour.html) in this game object.

The receiving method can choose to ignore the argument by having zero
arguments. If options is set to
[SendMessageOptions.RequireReceiver](SendMessageOptions.RequireReceiver.html)
an error is printed when the message is not picked up by any component.  
  
Note that messages will not be sent to inactive objects (ie, those that have
been deactivated in the editor or with the
[GameObject.SetActive](GameObject.SetActive.html) function).

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            /// Calls the function ApplyDamage with a value of 5
            SendMessage("ApplyDamage", 5.0);
        }  
      
        // Every script attached to the game object
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

