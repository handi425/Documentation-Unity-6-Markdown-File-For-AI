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

#  [GameObject](GameObject.html).GetComponentAtIndex

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

public [Component](Component.html) GetComponentAtIndex(int index);

### Parameters

index | The index position in the array of components at which to find the requested object.  
---|---  
  
### Returns

**Component** A reference to a component at the specified index. If no
component is found at the specified index, returns `null`.

### Description

Retrieves a reference to a component at a specified index of the GameObject's
array of components.

Using `GetComponentAtIndex` is a stable way to access components on a
GameObject because the index of a component stays the same unless components
are added or removed.  
  
An example use case for this is during UI development. This method throws an
exception if the index is out of bounds. Refer to
[GameObject.GetComponentCount](GameObject.GetComponentCount.html) for more
information.

    
    
    using UnityEngine;  
      
    public class GetComponentAtIndexExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) otherGameObject;  
      
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = otherGameObject.GetComponentAtIndex(5) as [HingeJoint](HingeJoint.html);  
      
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponents](GameObject.GetComponents.html)

* * *

## Declaration

public T GetComponentAtIndex(int index);

### Parameters

index | The index position in the array of components at which to find the requested object.  
---|---  
  
### Returns

**T** A reference to a component of type `T` at the specified index. If no
component is found at the specified index, returns `null`.

### Description

Retrieves a reference to a component of type T at a specific index on the
specified GameObject.

Using `GetComponentAtIndex` is a stable way to access components on a
GameObject because the index of a component stays the same unless components
are added or removed.  
  
An example use case for this is during UI development. This method throws an
exception if the index is out of bounds.  
  
Additional resources:
[GameObject.GetComponentCount](GameObject.GetComponentCount.html)

    
    
    using UnityEngine;  
      
    public class GetTComponentAtIndexExample : [MonoBehaviour](MonoBehaviour.html)
    {
        public [GameObject](GameObject.html) otherGameObject;  
      
        void Start()
        {
            [HingeJoint](HingeJoint.html) hinge = otherGameObject.GetComponentAtIndex<[HingeJoint](HingeJoint.html)>(5);  
      
            if (hinge != null)
            {
                hinge.useSpring = false;
            }
        }
    }
    

Additional resources: [Component](Component.html),
[GameObject.GetComponents](GameObject.GetComponents.html)

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

