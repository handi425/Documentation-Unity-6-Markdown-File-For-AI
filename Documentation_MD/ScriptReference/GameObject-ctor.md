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

# GameObject Constructor

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

public GameObject();

## Declaration

public GameObject(string name);

## Declaration

public GameObject(string name, params Type[] components);

### Parameters

name | The name of the [GameObject](GameObject.html), specified as a string. The name is stored in the [name](Object-name.html) property of the GameObject.  
---|---  
components | The components to attach, specified as an array of types that inherit from `Component`.  
  
### Description

Creates a new GameObject, with optional parameters to specify a name and set
of components to attach.

Use the constructor with no arguments to create a GameObject with an empty
`name` property and only a `Transform` component attached.  
  
Use the constructor with `name` parameter to create a GameObject with the
specified value as the name property and only a `Transform` component
attached.  
  
Use the constructor with `name` and `components` parameters to create a
GameObject with the specified name and the specified components attached, in
addition to the `Transform` component.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private void Start()
        {
            [GameObject](GameObject.html) exampleOne = new [GameObject](GameObject.html)();
            exampleOne.name = "GameObject1";
            exampleOne.AddComponent<[Rigidbody](Rigidbody.html)>();  
      
            [GameObject](GameObject.html) exampleTwo = new [GameObject](GameObject.html)("GameObject2");
            exampleTwo.AddComponent<[Rigidbody](Rigidbody.html)>();  
      
            [GameObject](GameObject.html) exampleThree = new [GameObject](GameObject.html)("GameObject3", typeof([Rigidbody](Rigidbody.html)), typeof([BoxCollider](BoxCollider.html)));
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

