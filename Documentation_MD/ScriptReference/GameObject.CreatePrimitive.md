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

#  [GameObject](GameObject.html).CreatePrimitive

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

public static [GameObject](GameObject.html)
CreatePrimitive([PrimitiveType](PrimitiveType.html) type);

### Parameters

type | The type of primitive object to create, specified as a member of the [PrimitiveType](PrimitiveType.html) enum.  
---|---  
  
### Description

Creates a GameObject of the specified PrimtiveType with a mesh renderer and
appropriate collider.

For `CreatePrimitive` to succeed at runtime, your project must reference the
following components:

  * [MeshFilter](MeshFilter.html)
  * [MeshRenderer](MeshRenderer.html)
  * [BoxCollider](BoxCollider.html)
  * [SphereCollider](SphereCollider.html)

To ensure you have the required references, declare private properties of
these types to prevent them being stripped from the build. Your project must
also reference the Default-Material. If it doesn't, the primitive object will
be shown in pink to indicate the missing material.  
  
For more information, refer to [Primitive and placeholder
objects](../Manual/PrimitiveObjects.html) in the Manual.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        // Create a plane, sphere and cube in the [Scene](SceneManagement.Scene.html).  
      
        void Start()
        {
            [GameObject](GameObject.html) plane  = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));  
      
            [GameObject](GameObject.html) cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            cube.transform.position = new [Vector3](Vector3.html)(0, 0.5f, 0);  
      
            [GameObject](GameObject.html) sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere.transform.position = new [Vector3](Vector3.html)(0, 1.5f, 0);  
      
            [GameObject](GameObject.html) capsule = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Capsule](PrimitiveType.Capsule.html));
            capsule.transform.position = new [Vector3](Vector3.html)(2, 1, 0);  
      
            [GameObject](GameObject.html) cylinder = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cylinder](PrimitiveType.Cylinder.html));
            cylinder.transform.position = new [Vector3](Vector3.html)(-2, 1, 0);
        }
    }
    

Additional resources: [PrimitiveType](PrimitiveType.html)

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

