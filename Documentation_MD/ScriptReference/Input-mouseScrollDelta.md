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

#  [Input](Input.html).mouseScrollDelta

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

public static [Vector2](Vector2.html) mouseScrollDelta;

### Description

The current mouse scroll delta. (Read Only)

**Note: This API is part of the legacy** `Input` **class, and not recommended
for new projects. The documentation is provided here to support legacy
projects that use the old Input Manager and Input class. For new projects you
should use the newer and Input System Package**. ([read
more](../Manual/Input.html)).  
  
[Input.mouseScrollDelta](Input-mouseScrollDelta.html) is stored in a
[Vector2.y](Vector2-y.html) property. (The [Vector2.x](Vector2-x.html) value
is ignored.) [Input.mouseScrollDelta](Input-mouseScrollDelta.html) can be
positive (up) or negative (down). The value is zero when the mouse scroll is
not rotated. Note that a mouse with a center scroll wheel is typical on a PC.
Modern `macOS` uses double finger movement up and down on the trackpad to
emulate center scrolling. The value returned by [mouseScrollDelta](Input-
mouseScrollDelta.html) will need to be adjusted according to the scroll rate.
In the example below a `scale` of `0.1f` is used.  
  
Note that [mouseScrollDelta](Input-mouseScrollDelta.html) is read-only.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Input.mouseScrollDelta](Input-mouseScrollDelta.html) example
    //
    // Create a sphere moved by a mouse scrollwheel or two-finger
    // slide on a Mac trackpad.  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Transform](Transform.html) sphere;
        private float scale;  
      
        void Awake()
        {
            [GameObject](GameObject.html) go = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere = go.transform;  
      
            // create a yellow quad
            go = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Quad](PrimitiveType.Quad.html));
            go.transform.Rotate(new [Vector3](Vector3.html)(90.0f, 0.0f, 0.0f));
            go.transform.localScale = new [Vector3](Vector3.html)(4.0f, 4.0f, 4.0f);
            go.GetComponent<[Renderer](Renderer.html)>().material.color = new [Color](Color.html)(0.75f, 0.75f, 0.0f, 0.5f);  
      
            // change the camera color and position
            Camera.main.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);
            Camera.main.transform.position = new [Vector3](Vector3.html)(2, 1, 5);
            Camera.main.transform.Rotate(0, -160, 0);  
      
            scale = 0.1f;
        }  
      
        void OnGUI()
        {
            [Vector3](Vector3.html) pos = sphere.position;
            pos.y += Input.mouseScrollDelta.y * scale;
            sphere.position = pos;
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

