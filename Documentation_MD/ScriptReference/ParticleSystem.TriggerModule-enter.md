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

#  [ParticleSystem.TriggerModule](ParticleSystem.TriggerModule.html).enter

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

public [ParticleSystemOverlapAction](ParticleSystemOverlapAction.html) enter;

### Description

Choose what action to perform when particles enter the trigger volume.

Additional resources:
[MonoBehaviour.OnParticleTrigger](MonoBehaviour.OnParticleTrigger.html).

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using System.Collections.Generic;
    using UnityEngine.EventSystems;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool enter;
        public bool exit;
        public bool inside;
        public bool outside;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var sphere = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Sphere](PrimitiveType.Sphere.html));
            sphere.transform.parent = ps.transform;
            sphere.transform.localPosition = new [Vector3](Vector3.html)(0.0f, 0.0f, 3.0f);
            sphere.transform.localScale = new [Vector3](Vector3.html)(3.0f, 3.0f, 3.0f);
            sphere.GetComponent<[MeshRenderer](MeshRenderer.html)>().material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Particles/Standard Unlit"));  
      
            var shape = ps.shape;
            shape.enabled = false;  
      
            var trigger = ps.trigger;
            trigger.enabled = true;
            trigger.SetCollider(0, sphere.GetComponent<[Collider](Collider.html)>());
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var trigger = ps.trigger;
            trigger.enter = enter ? [ParticleSystemOverlapAction.Callback](ParticleSystemOverlapAction.Callback.html) : [ParticleSystemOverlapAction.Ignore](ParticleSystemOverlapAction.Ignore.html);
            trigger.exit = exit ? [ParticleSystemOverlapAction.Callback](ParticleSystemOverlapAction.Callback.html) : [ParticleSystemOverlapAction.Ignore](ParticleSystemOverlapAction.Ignore.html);
            trigger.inside = inside ? [ParticleSystemOverlapAction.Callback](ParticleSystemOverlapAction.Callback.html) : [ParticleSystemOverlapAction.Ignore](ParticleSystemOverlapAction.Ignore.html);
            trigger.outside = outside ? [ParticleSystemOverlapAction.Callback](ParticleSystemOverlapAction.Callback.html) : [ParticleSystemOverlapAction.Ignore](ParticleSystemOverlapAction.Ignore.html);
        }  
      
        void OnGUI()
        {
            enter = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 40, 200, 30), enter, "Enter Callback");
            exit = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 80, 200, 30), exit, "Exit Callback");
            inside = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 120, 200, 30), inside, "Inside Callback");
            outside = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 160, 200, 30), outside, "Outside Callback");
        }  
      
        void OnParticleTrigger()
        {
            if (enter)
            {
                List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> enterList = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();
                int numEnter = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Enter](ParticleSystemTriggerEventType.Enter.html), enterList);  
      
                for (int i = 0; i < numEnter; i++)
                {
                    [ParticleSystem.Particle](ParticleSystem.Particle.html) p = enterList[i];
                    p.startColor = new [Color32](Color32.html)(255, 0, 0, 255);
                    enterList[i] = p;
                }  
      
                ps.SetTriggerParticles([ParticleSystemTriggerEventType.Enter](ParticleSystemTriggerEventType.Enter.html), enterList);
            }  
      
            if (exit)
            {
                List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> exitList = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();
                int numExit = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Exit](ParticleSystemTriggerEventType.Exit.html), exitList);  
      
                for (int i = 0; i < numExit; i++)
                {
                    [ParticleSystem.Particle](ParticleSystem.Particle.html) p = exitList[i];
                    p.startColor = new [Color32](Color32.html)(0, 255, 0, 255);
                    exitList[i] = p;
                }  
      
                ps.SetTriggerParticles([ParticleSystemTriggerEventType.Exit](ParticleSystemTriggerEventType.Exit.html), exitList);
            }  
      
            if (inside)
            {
                List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> insideList = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();
                int numInside = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Inside](ParticleSystemTriggerEventType.Inside.html), insideList);  
      
                for (int i = 0; i < numInside; i++)
                {
                    [ParticleSystem.Particle](ParticleSystem.Particle.html) p = insideList[i];
                    p.startColor = new [Color32](Color32.html)(0, 0, 255, 255);
                    insideList[i] = p;
                }  
      
                ps.SetTriggerParticles([ParticleSystemTriggerEventType.Inside](ParticleSystemTriggerEventType.Inside.html), insideList);
            }  
      
            if (outside)
            {
                List<[ParticleSystem.Particle](ParticleSystem.Particle.html)> outsideList = new List<[ParticleSystem.Particle](ParticleSystem.Particle.html)>();
                int numOutside = ps.GetTriggerParticles([ParticleSystemTriggerEventType.Outside](ParticleSystemTriggerEventType.Outside.html), outsideList);  
      
                for (int i = 0; i < numOutside; i++)
                {
                    [ParticleSystem.Particle](ParticleSystem.Particle.html) p = outsideList[i];
                    p.startColor = new [Color32](Color32.html)(0, 255, 255, 255);
                    outsideList[i] = p;
                }  
      
                ps.SetTriggerParticles([ParticleSystemTriggerEventType.Outside](ParticleSystemTriggerEventType.Outside.html), outsideList);
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

