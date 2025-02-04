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

#  [Object](Object.html).Destroy

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

## Declaration

public static void Destroy([Object](Object.html) obj, float t = 0.0F);

### Parameters

obj | The object to destroy.  
---|---  
t | The optional amount of time to delay before destroying the object.  
  
### Description

Removes a GameObject, component or asset.

The object `obj` is destroyed immediately after the current Update loop, or
`t` seconds from now if a time is specified. If `obj` is a
[Component](Component.html), this method removes the component from the
[GameObject](GameObject.html) and destroys it. If `obj` is a
[GameObject](GameObject.html), it destroys the [GameObject](GameObject.html),
all its components and all transform children of the
[GameObject](GameObject.html). Actual object destruction is always delayed
until after the current Update loop, but is always done before rendering.  
  
Note: When destroying MonoBehaviour scripts, Unity calls OnDisable and
OnDestroy before the script is removed.  
  
Additional resources: [Object.DestroyImmediate](Object.DestroyImmediate.html)

    
    
    using UnityEngine;  
      
    public class ScriptExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void DestroyGameObject()
        {
            Destroy(gameObject);
        }  
      
        void DestroyScriptInstance()
        {
            // Removes this script instance from the game object
            Destroy(this);
        }  
      
        void DestroyComponent()
        {
            // Removes the rigidbody from the game object
            Destroy(GetComponent<[Rigidbody](Rigidbody.html)>());
        }  
      
        void DestroyObjectDelayed()
        {
            // Kills the game object in 5 seconds after loading the object
            Destroy(gameObject, 5);
        }  
      
        // When the user presses Ctrl, it will remove the
        // [BoxCollider](BoxCollider.html) component from the game object
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Input.GetButton](Input.GetButton.html)("Fire1") && GetComponent<[BoxCollider](BoxCollider.html)>())
            {
                Destroy(GetComponent<[BoxCollider](BoxCollider.html)>());
            }
        }
    }
    

Destroy is inherited from the UnityEngine.Object base class.

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

