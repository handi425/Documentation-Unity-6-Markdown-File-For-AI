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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).flip

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

public [Vector3](Vector3.html) flip;

### Description

Flip a percentage of the particles, along each axis.

Set between 0 and 1, where higher values cause a higher proportion of the
particles to flip, and 1 causes all particles to flip.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {  
      
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;
        public [Vector3](Vector3.html) flip;  
      
        void Start() {  
      
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            psr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));  // square material so we can see the pivot more easily
            psr.mesh = Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Capsule.fbx");
        }  
      
        void [Update](PlayerLoop.Update.html)() {  
      
            psr.flip = flip;
        }  
      
        void OnGUI() {  
      
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "X");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Y");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "Z");  
      
            flip.x = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(65, 25, 100, 30), flip.x, 0.0f, 1.0f);
            flip.y = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(65, 65, 100, 30), flip.y, 0.0f, 1.0f);
            flip.z = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(65, 105, 100, 30), flip.z, 0.0f, 1.0f);
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

