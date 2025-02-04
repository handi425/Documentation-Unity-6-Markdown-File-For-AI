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

#  [GameObject](GameObject.html).GetComponentInParent

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

public T GetComponentInParent(bool includeInactive = false);

### Parameters

includeInactive | Whether to include inactive parent GameObjects in the search.  
---|---  
  
### Returns

**T** A Component of the matching type `T`, otherwise `null` if no matching
Component is found.

### Description

Retrieves a reference to a component of type T on the specified GameObject, or
any parent of the GameObject.

This method checks the GameObject on which it is called first, then recurses
upwards through each parent GameObject, until it finds a matching Component of
the specified type `T`.  
  
Only active parent GameObjects are included in the search, unless you call the
method with the `includeInactive` parameter set to `true`, in which case
inactive parent GameObjects are also included. The GameObject on which the
method is called is always searched regardless of this parameter.  
  
The typical usage for this method is to call it on a reference to a different
GameObject than the one your script is on. For example:  
  
`myResults = otherGameObject.GetComponentInParent<ComponentType>()`  
  
However, if you're writing code inside a MonoBehaviour class, you can omit the
preceding GameObject reference to perform the search on the same GameObject
your script is attached to, and its parents. In this instance, you're actually
calling [Component.GetComponentInParent](Component.GetComponentInParent.html)
because the script itself is a type of component, but the result is the same
as if you'd referenced the GameObject itself. For example:  
  
`myResults = GetComponentInParent<ComponentType>()`  
  
`GetComponentInParent` returns only the first matching component found, and
components are not checked in a defined order. If there are multiple
components of the specified type and you need to find a specific one, you
should use
[Component.GetComponentsInParent](Component.GetComponentsInParent.html) and
check the list of components returned to identify the one you want.  
  
To find components attached to other GameObjects, you need a [reference to
that other GameObject](../Manual/class-
GameObject.html#AccessingOtherGameObjects) (or any component attached to that
GameObject). You can then call `GetComponentInParent` on that reference.  
  
**Note** : If the type you request is a derivative of MonoBehaviour and the
associated script can't be loaded then this function will return `null` for
that component.  
  
The following example gets a reference to a hinge joint component on the
referenced GameObject or any of its parents, and if found, sets a property on
that hinge joint component.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class GetComponentInParentExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // Disable the spring on the first [HingeJoint](HingeJoint.html) component found on the referenced [GameObject](GameObject.html) or any of its parents  
      
        public [GameObject](GameObject.html) objectToCheck;  
      
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = objectToCheck.GetComponentInParent<[HingeJoint](HingeJoint.html)>();  
      
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponentsInChildren](GameObject.GetComponentsInChildren.html)

* * *

## Declaration

public [Component](Component.html) GetComponentInParent(Type type);

## Declaration

public [Component](Component.html) GetComponentInParent(Type type, bool
includeInactive);

### Parameters

type | The type of component to search for.  
---|---  
includeInactive | Whether to include inactive parent GameObjects in the search.  
  
### Returns

**Component** A Component of the matching `type`, otherwise `null` if no
matching Component is found.

### Description

The non-generic version of this method.

This version of `GetComponentInParent` is not as efficient as the Generic
version (above), so you should only use it if necessary.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class GetComponentInParentExample : [MonoBehaviour](MonoBehaviour.html)
    {
        // Disable the spring on the first [HingeJoint](HingeJoint.html) component found on the referenced [GameObject](GameObject.html) or any of its parents  
      
        public [GameObject](GameObject.html) objectToCheck;  
      
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = objectToCheck.GetComponentInParent(typeof([HingeJoint](HingeJoint.html))) as [HingeJoint](HingeJoint.html);  
      
            if (hinge != null)
            {
                hinge.useSpring = false;
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

