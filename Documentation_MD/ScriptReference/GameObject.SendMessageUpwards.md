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

#  [GameObject](GameObject.html).SendMessageUpwards

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

[Switch to Manual](../Manual/class-GameObject.html "Go to GameObject Component
in the Manual")

## Declaration

public void SendMessageUpwards(string methodName, object value = null,
[SendMessageOptions](SendMessageOptions.html) options =
SendMessageOptions.RequireReceiver);

### Parameters

methodName | The name of the MonoBehaviour method to call.  
---|---  
value | An optional parameter value to pass to the called method.  
options | Whether an error should be raised if the method doesn't exist on the target object.  
  
### Description

Calls the specified method on every MonoBehaviour attached to the GameObject
and on every ancestor of the behaviour.

A `value` parameter specified for a method that doesn't accept parameters is
ignored. If `options` is set to
[SendMessageOptions.RequireReceiver](SendMessageOptions.RequireReceiver.html)
an error is printed when the message is not picked up by any component.  
  
**Note** : Messages are not sent to MonoBehaviours attached to objects for
which [GameObject.activeSelf](GameObject-activeSelf.html) or
[GameObject.activeInHierarchy](GameObject-activeInHierarchy.html) are `false`.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Calls the function ApplyDamage with a value of 5
            gameObject.SendMessageUpwards("ApplyDamage", 5.0);
        }
    }  
      
    public class Example2 : [MonoBehaviour](MonoBehaviour.html)
    {
        public void ApplyDamage(float damage)
        {
            print(damage);
        }
    }
    

Additional resources: [MonoBehaviour](MonoBehaviour.html),
[GameObject.SendMessage](GameObject.SendMessage.html)

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

