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

#  [ParticleSystemRenderer](ParticleSystemRenderer.html).alignment

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

public [ParticleSystemRenderSpace](ParticleSystemRenderSpace.html) alignment;

### Description

Control the direction that particles face.

For many applications, it is beneficial for particles to always face the
Camera. This property allows you to change whether particles in the system
face the Camera or not.  
  
Particles can face the Camera in two ways:  
  
1) Aligned to the Camera plane, so that all particles are aligned with the
same facing direction.  
2) Aligned individually to face the eye position, which can be more convincing
for particles that approach the Camera in close proximity or for VR
environments.  
  
Unaligned particles can be set to align to the world or to their local
transform, as required.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html) {  
      
        private [ParticleSystem](ParticleSystem.html) ps;
        private [ParticleSystemRenderer](ParticleSystemRenderer.html) psr;
        public [ParticleSystemRenderSpace](ParticleSystemRenderSpace.html) alignment = [ParticleSystemRenderSpace.View](ParticleSystemRenderSpace.View.html);  
      
        void Start() {  
      
            Camera.main.transform.rotation = [Quaternion.Euler](Quaternion.Euler.html)(0.0f, 20.0f, 0.0f);   // rotate the camera so we can see the difference between view and world space  
      
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            psr = GetComponent<[ParticleSystemRenderer](ParticleSystemRenderer.html)>();  
      
            var main = ps.main;
            main.startSpeed = 2.0f;  
      
            psr.material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Sprites/Default"));
        }  
      
        void [Update](PlayerLoop.Update.html)() {
            psr.alignment = alignment;
        }  
      
        void OnGUI() {
            alignment = ([ParticleSystemRenderSpace](ParticleSystemRenderSpace.html))[GUI.SelectionGrid](GUI.SelectionGrid.html)(new [Rect](Rect.html)(25, 25, 300, 30), (int)alignment, new [GUIContent](GUIContent.html)[] { new [GUIContent](GUIContent.html)("View"), new [GUIContent](GUIContent.html)("World"), new [GUIContent](GUIContent.html)("Local"), new [GUIContent](GUIContent.html)("Facing") }, 4);
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

