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

#  [ParticleSystem.TrailModule](ParticleSystem.TrailModule.html).worldSpace

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

public bool worldSpace;

### Description

Drop new trail points in world space, regardless of Particle System Simulation
Space.

When set to true, trails are always in world space, and do not move relative
to the Transform component. When set to false, trails move with the Particle
System Transform, if also using local Simulation Space. Additional resources:
[ParticleSystem.MainModule.simulationSpace](ParticleSystem.MainModule-
simulationSpace.html).

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool worldSpace = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startColor = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)([Color.red](Color-red.html), [Color.yellow](Color-yellow.html));
            main.startSize = 0.1f;
            main.startLifetime = 0.5f;  
      
            var trails = ps.trails;
            trails.enabled = true;  
      
            var psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            psr.trailMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            ps.transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html) * 2.0f) * 2.0f, 0.0f, 0.0f);  
      
            var trails = ps.trails;
            trails.worldSpace = worldSpace;
        }  
      
        void OnGUI()
        {
            worldSpace = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 25, 200, 30), worldSpace, "World [Space](Space.html)");
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

