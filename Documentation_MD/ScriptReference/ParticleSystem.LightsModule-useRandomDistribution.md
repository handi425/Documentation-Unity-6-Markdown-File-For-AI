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

#
[ParticleSystem.LightsModule](ParticleSystem.LightsModule.html).useRandomDistribution

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

[Switch to Manual](../Manual/class-ParticleSystem.html "Go to ParticleSystem
Component in the Manual")

public bool useRandomDistribution;

### Description

Randomly assign Lights to new particles based on
[ParticleSystem.LightsModule.ratio](ParticleSystem.LightsModule-ratio.html).

When this property is false, the system assigns Lights at regular intervals
according to the
[ParticleSystem.LightsModule.ratio](ParticleSystem.LightsModule-ratio.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    // For best results, use Deferred Rendering (see [Camera](Camera.html) settings)
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public [Light](Light.html) lightPrefab;     // Provide a light Prefab in the inspector
        public float hSliderValueRatio = 1.0f;
        public float hSliderValueMax = 1000.0f;
        public bool randomDistribution = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            ps.transform.localRotation = [Quaternion.Euler](Quaternion.Euler.html)(0.0f, 0.0f, 45.0f);  
      
            var shape = ps.shape;
            shape.shapeType = [ParticleSystemShapeType.Circle](ParticleSystemShapeType.Circle.html);  
      
            var lights = ps.lights;
            lights.enabled = true;
            lights.light = lightPrefab;  
      
            // plane to receive lights
            var plane = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Plane](PrimitiveType.Plane.html));
            plane.transform.parent = ps.transform;
            plane.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 3.0f);
            plane.transform.localScale = new [Vector3](Vector3.html)(20.0f, 20.0f, 20.0f);
            plane.transform.localRotation = [Quaternion.Euler](Quaternion.Euler.html)(-90.0f, 0.0f, 0.0f);  
      
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            material.color = new [Color](Color.html)(0.1f, 0.1f, 0.1f, 1.0f);
            plane.GetComponent<[MeshRenderer](MeshRenderer.html)>().material = material;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var lights = ps.lights;
            lights.ratio = hSliderValueRatio;
            lights.maxLights = (int)hSliderValueMax;
            lights.useRandomDistribution = randomDistribution;
        }  
      
        void OnGUI()
        {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 100, 30), "Ratio");
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "Max Lights");  
      
            hSliderValueRatio = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 45, 100, 30), hSliderValueRatio, 0.0f, 1.0f);
            hSliderValueMax = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(95, 85, 100, 30), hSliderValueMax, 0.0f, 500.0f);  
      
            randomDistribution = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 125, 400, 30), randomDistribution, "Randomly assign Lights to Particles instead of evenly distributing them.");
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

