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

#  [GameObject](GameObject.html).AddComponent

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

public [Component](Component.html) AddComponent(Type componentType);

### Description

Adds a component of the specified type to the GameObject.

There is no corresponding method for removing a component from a GameObject.
To remove a component, use [Object.Destroy](Object.Destroy.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class AddComponentExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [SphereCollider](SphereCollider.html) sc = gameObject.AddComponent(typeof([SphereCollider](SphereCollider.html))) as [SphereCollider](SphereCollider.html);
        }
    }
    

Additional resources: [Component](Component.html),
[Object.Destroy](Object.Destroy.html)

* * *

## Declaration

public T AddComponent();

### Description

Generic version of this method.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class AddComponentExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [SphereCollider](SphereCollider.html) sc = gameObject.AddComponent<[SphereCollider](SphereCollider.html)>();
        }
    }
    

Additional resources: [Component](Component.html),
[Object.Destroy](Object.Destroy.html)

* * *

**Obsolete** GameObject.AddComponent with string argument has been deprecated.
Use GameObject.AddComponent<T>() instead.

## Declaration

public [Component](Component.html) AddComponent(string className);

### Description

Adds a component of the specified class name to the GameObject.

Deprecated: Use AddComponent(Type) or the generic version of this method
instead.

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

