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
[ParticleSystem.TrailModule](ParticleSystem.TrailModule.html).splitSubEmitterRibbons

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

public bool splitSubEmitterRibbons;

### Description

Specifies whether, if you use this system as a sub-emitter, ribbons connect
particles from each parent particle independently.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystem](ParticleSystem.html) sps;
        public bool splitSubEmitterRibbons = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.startColor = new [ParticleSystem.MinMaxGradient](ParticleSystem.MinMaxGradient.html)([Color.red](Color-red.html), [Color.yellow](Color-yellow.html));
            main.startSize = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.01f, 1.0f);
            main.startLifetime = 1.5f;  
      
            sps = new [GameObject](GameObject.html)("SubEmitter", typeof([ParticleSystem](ParticleSystem.html))).GetComponent<[ParticleSystem](ParticleSystem.html)>();
            sps.transform.parent = ps.transform;  
      
            var sub = ps.subEmitters;
            sub.enabled = true;
            sub.AddSubEmitter(sps, [ParticleSystemSubEmitterType.Birth](ParticleSystemSubEmitterType.Birth.html), [ParticleSystemSubEmitterProperties.InheritColor](ParticleSystemSubEmitterProperties.InheritColor.html));  
      
            var smain = sps.main;
            smain.startSpeed = 0.0f;  
      
            var sshape = sps.shape;
            sshape.enabled = false;  
      
            var strails = sps.trails;
            strails.enabled = true;
            strails.mode = [ParticleSystemTrailMode.Ribbon](ParticleSystemTrailMode.Ribbon.html);
            strails.widthOverTrail = 0.1f;  
      
            var spsr = sps.GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();
            spsr.renderMode = [ParticleSystemRenderMode.None](ParticleSystemRenderMode.None.html);
            spsr.trailMaterial = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var strails = sps.trails;
            strails.splitSubEmitterRibbons = splitSubEmitterRibbons;
        }  
      
        void OnGUI()
        {
            splitSubEmitterRibbons = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 25, 200, 30), splitSubEmitterRibbons, "Split Sub Emitter Ribbons");
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

