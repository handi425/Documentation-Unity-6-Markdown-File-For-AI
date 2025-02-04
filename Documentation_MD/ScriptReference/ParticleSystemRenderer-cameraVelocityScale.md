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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).cameraVelocityScale

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

public float cameraVelocityScale;

### Description

How much do the particles stretch depending on the [Camera](Camera.html)'s
speed.

Use this to make particles become larger if the viewing Camera has a large
speed.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {  
      
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;
        public [ParticleSystemRenderMode](ParticleSystemRenderMode.html) renderMode = [ParticleSystemRenderMode.Billboard](ParticleSystemRenderMode.Billboard.html);
        public float cameraScale = 0.0f;
        public float lengthScale = 0.0f;
        public float velocityScale = 1.0f;  
      
        void Start() {  
      
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            psr.mesh = Resources.GetBuiltinResource<[Mesh](Mesh.html)>("Capsule.fbx");  
      
            var main = ps.main;
            main.startSpeed = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.5f, 1.5f);
            main.startSize = new [ParticleSystem.MinMaxCurve](ParticleSystem.MinMaxCurve.html)(0.1f, 0.8f);
        }  
      
        void [Update](PlayerLoop.Update.html)() {
            psr.renderMode = renderMode;
            psr.cameraVelocityScale = cameraScale;
            psr.lengthScale = lengthScale;
            psr.velocityScale = velocityScale;  
      
            if (renderMode == [ParticleSystemRenderMode.Stretch](ParticleSystemRenderMode.Stretch.html))
                Camera.main.transform.position = new [Vector3](Vector3.html)([Mathf.Sin](Mathf.Sin.html)([Time.time](Time-time.html)) * 4.0f, 0.0f, -10.0f);    // move the camera so we can see the effect on stretch camera velocity
        }  
      
        void OnGUI() {
            renderMode = ([ParticleSystemRenderMode](ParticleSystemRenderMode.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 25, 900, 30), (int)renderMode, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("Billboard"), new [GUIContent](GUIContent.html)("Stretch"), new [GUIContent](GUIContent.html)("HorizontalBillboard"), new [GUIContent](GUIContent.html)("VerticalBillboard"), new [GUIContent](GUIContent.html)("[Mesh](Mesh.html)"), new [GUIContent](GUIContent.html)("None") }, 6);  
      
            if (renderMode == [ParticleSystemRenderMode.Stretch](ParticleSystemRenderMode.Stretch.html)) {  
      
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 80, 100, 30), "[Camera](Camera.html) [Scale](UIElements.Scale.html)");
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 120, 100, 30), "[Length](UIElements.Length.html) [Scale](UIElements.Scale.html)");
                [GUI.Label](GUI.Label.html)(new [Rect](Rect.html)(25, 160, 100, 30), "Velocity [Scale](UIElements.Scale.html)");  
      
                cameraScale = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 85, 100, 30), cameraScale, 0.0f, 10.0f);
                lengthScale = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 125, 100, 30), lengthScale, 0.0f, 10.0f);
                velocityScale = [GUI.HorizontalSlider](GUI.HorizontalSlider.html)(new [Rect](Rect.html)(125, 165, 100, 30), velocityScale, 0.0f, 10.0f);
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

