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

#  [Transform](Transform.html).localScale

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

public [Vector3](Vector3.html) localScale;

### Description

The scale of the transform relative to the GameObjects parent.

The example below creates a sphere [GameObject](GameObject.html) with a scale
of (1,1,1). The application then changes the [Transform.localScale](Transform-
localScale.html) from 1.0 down to 0.25 and back to 1.0 repeatedly.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [GameObject](GameObject.html) sphere;
        private [Vector3](Vector3.html) scaleChange, positionChange;  
      
        void Awake()
        {
            Camera.main.clearFlags = [CameraClearFlags.SolidColor](CameraClearFlags.SolidColor.html);  
      
            // Create a sphere at the origin.
            sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere.transform.position = new [Vector3](Vector3.html)(0, 0, 0);  
      
            // Create a plane and move down by 0.5.
            [GameObject](GameObject.html) plane = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));
            plane.transform.position = new [Vector3](Vector3.html)(0, -0.5f, 0);  
      
            // Change the floor color to blue.
            // The blue material is present in [Resources](Resources.html) and not created in this script.
            [Renderer](Renderer.html) rend = plane.GetComponent<[Renderer](Renderer.html)>();
            rend.material = [Resources.Load](Resources.Load.html)<[Material](Material.html)>("blue");  
      
            scaleChange = new [Vector3](Vector3.html)(-0.01f, -0.01f, -0.01f);
            positionChange = new [Vector3](Vector3.html)(0.0f, -0.005f, 0.0f);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            sphere.transform.localScale += scaleChange;
            sphere.transform.position += positionChange;  
      
            // Move upwards when the sphere hits the floor or downwards
            // when the sphere scale extends 1.0f.
            if (sphere.transform.localScale.y < 0.1f || sphere.transform.localScale.y > 1.0f)
            {
                scaleChange = -scaleChange;
                positionChange = -positionChange;
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

