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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).SetMeshWeightings

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

## Declaration

public void SetMeshWeightings(float[] weightings, int size);

## Declaration

public void SetMeshWeightings(float[] weightings);

### Parameters

weightings | The array of weights to use.  
---|---  
size | The number of elements from the weighting array to apply.  
  
### Description

Sets the weights that the
[ParticleSystemRenderer](ParticleSystemRenderer.html) uses to assign Meshes to
particles.

The [ParticleSystemRenderer](ParticleSystemRenderer.html) only uses these
weights if you set [ParticleSystemRenderer.renderMode](ParticleSystemRenderer-
renderMode.html) to
[ParticleSystemRenderMode.Mesh](ParticleSystemRenderMode.Mesh.html) and set
[ParticleSystemRenderer.meshDistribution](ParticleSystemRenderer-
meshDistribution.html) to
[ParticleSystemMeshDistribution.NonUniformRandom](ParticleSystemMeshDistribution.NonUniformRandom.html).

The weightings are relative to each other but can be any positive value. For
example, if you set the weights to 6 and 3, the ParticleSystemRenderer
randomly selects the first Mesh approximately twice as often as the second
Mesh. It can be most intuitive to use percentages for the weightings and
ensure that the sum of the weightings adds up to 100, but this is not a
requirement.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;  
      
        void Start() {  
      
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            psr.renderMode = [ParticleSystemRenderMode.Mesh](ParticleSystemRenderMode.Mesh.html);
            psr.meshDistribution = [ParticleSystemMeshDistribution.NonUniformRandom](ParticleSystemMeshDistribution.NonUniformRandom.html);
            psr.SetMeshes(new [Mesh](Mesh.html)[]{ Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Capsule.fbx"), Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Cube.fbx"), Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Sphere.fbx") });
            psr.SetMeshWeightings(new float[]{ 0.1f, 0.1f, 0.8f });
        }  
      
        void OnGUI() {
            [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 40, 200, 30), "[Mesh](Mesh.html) Count: " + psr.meshCount.ToString());
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

