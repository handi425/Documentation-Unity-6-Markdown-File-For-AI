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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).enableGPUInstancing

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

public bool enableGPUInstancing;

### Description

Enables GPU Instancing on platforms that support it.

To use GPU Instancing to render a Particle System, the particle must use a
Shader that contains a Procedural Instancing pass (that is, it contains the
`#pragma instancing_options procedural` directive).

    
    
    using UnityEngine;
    using System.Collections;
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;
        private bool enableGPUInstancing = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            psr.renderMode = [ParticleSystemRenderMode.Mesh](ParticleSystemRenderMode.Mesh.html);
            psr.SetMeshes(new [Mesh](Mesh.html)[] { Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Capsule.fbx"), Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Cube.fbx"), Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Sphere.fbx") });  
      
            psr.sharedMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Surface"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            psr.enableGPUInstancing = enableGPUInstancing;
        }  
      
        void OnGUI()
        {
            enableGPUInstancing = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 45, 200, 30), enableGPUInstancing, "Enabled");
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

