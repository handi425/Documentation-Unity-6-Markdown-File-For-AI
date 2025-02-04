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

#  [ParticleSystem.MainModule](ParticleSystem.MainModule.html).startSize3D

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

public bool startSize3D;

### Description

A flag to enable specifying particle size individually for each axis.

Additional resources: [MinMaxCurve](ParticleSystem.MinMaxCurve.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public float hSliderValueX = 1.0F;
        public float hSliderValueY = 1.0F;
        public float hSliderValueZ = 1.0F;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startSize3D = true;  
      
            var psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            psr.renderMode = [ParticleSystemRenderMode.Mesh](ParticleSystemRenderMode.Mesh.html);
            psr.mesh = Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Cube.fbx");// use a mesh, because billboards have no Z axis size
            psr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var main = ps.main;
            main.startSizeXMultiplier = hSliderValueX;
            main.startSizeYMultiplier = hSliderValueY;
            main.startSizeZMultiplier = hSliderValueZ;
        }  
      
        void OnGUI()
        {
            hSliderValueX = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 45, 100, 30), hSliderValueX, 0.0F, 360.0F * [Mathf.Deg2Rad](Mathf.Deg2Rad.html));
            hSliderValueY = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 75, 100, 30), hSliderValueY, 0.0F, 360.0F * [Mathf.Deg2Rad](Mathf.Deg2Rad.html));
            hSliderValueZ = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(25, 105, 100, 30), hSliderValueZ, 0.0F, 360.0F * [Mathf.Deg2Rad](Mathf.Deg2Rad.html));
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

