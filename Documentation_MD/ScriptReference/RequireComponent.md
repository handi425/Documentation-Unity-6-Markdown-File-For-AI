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

# RequireComponent

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

The RequireComponent attribute automatically adds required components as
dependencies.

When you add a script which uses RequireComponent to a GameObject, the
required component is automatically added to the GameObject. This is useful to
avoid setup errors. For example a script might require that a Rigidbody is
always added to the same GameObject. When you use RequireComponent, this is
done automatically, so you are unlikely to get the setup wrong.  
  
**Note:** RequireComponent only checks for missing dependencies when
[GameObject.AddComponent](GameObject.AddComponent.html) is called. This
happens both in the Editor, or at runtime. Unity does not automatically add
any missing dependences to the components with GameObjects that lack the new
dependencies.

    
    
    using UnityEngine;  
      
    // PlayerScript requires the [GameObject](GameObject.html) to have a [Rigidbody](Rigidbody.html) component
    [[RequireComponent](RequireComponent.html)(typeof([Rigidbody](Rigidbody.html)))]
    public class PlayerScript : [MonoBehaviour](MonoBehaviour.html)
    {
        [Rigidbody](Rigidbody.html) rb;  
      
        void Start()
        {
            rb = GetComponent<[Rigidbody](Rigidbody.html)>();
        }  
      
        void [FixedUpdate](PlayerLoop.FixedUpdate.html)()
        {
            rb.AddForce([Vector3.up](Vector3-up.html));
        }
    }
    

### Constructors

[RequireComponent](RequireComponent-ctor.html)| Require a single component.  
---|---  
  
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

