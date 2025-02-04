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

#  [GameObject](GameObject.html).TryGetComponent

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

public bool TryGetComponent(out T component);

### Parameters

component | The `out` parameter that will contain the component or `null`.  
---|---  
  
### Returns

**bool** Returns `true` if the component is found, `false` otherwise.

### Description

Retrieves the component of the specified type, if it exists.

`TryGetComponent` attempts to retrieve the component of the given type. The
notable difference compared to
[GameObject.GetComponent](GameObject.GetComponent.html) is that this method
does not allocate memory in the Editor when the requested component does not
exist.

    
    
    using UnityEngine;  
      
    public class TryGetComponentExample : [MonoBehaviour](MonoBehaviour.html)
    {
     
        public [GameObject](GameObject.html) objectToCheck;  
      
        void Start()
        {
            if (objectToCheck.TryGetComponent<[HingeJoint](HingeJoint.html)>(out [HingeJoint](HingeJoint.html) hinge))
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponent](GameObject.GetComponent.html)

* * *

## Declaration

public bool TryGetComponent(Type type, out [Component](Component.html)
component);

### Parameters

type | The type of component to search for.  
---|---  
component | The `out` parameter that will contain the component or `null`.  
  
### Returns

**bool** Returns `true` if the component is found, `false` otherwise.

### Description

The non-generic version of this method.

This version of `TryGetComponent` is not as efficient as the Generic version
(above), so you should only use it if necessary.

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

