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
[ParticleSystem.ShapeModule](ParticleSystem.ShapeModule.html).alignToDirection

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

public bool alignToDirection;

### Description

Align particles based on their initial direction of travel.

The Shape Module supports setting the initial rotation of particles based on
their direction of travel. This can be useful to make particles appear to have
originated from the surface of a Mesh (for example, paint flaking off a
surface). This works with any shape type. Unity applies any
ParticleSystem.startRotation on top of this setting, so you can use both
together.  
  
You can use this setting in conjunction with the
[ParticleSystem.MainModule.startRotation](ParticleSystem.MainModule-
startRotation.html) setting; Unity adds the rotation given by
[ParticleSystem.MainModule.startRotation](ParticleSystem.MainModule-
startRotation.html) on top of the value that
[ParticleSystem.ShapeModule.alignToDirection](ParticleSystem.ShapeModule-
alignToDirection.html) calculates.  
  
For example: add a
[ParticleSystem.MainModule.startRotation](ParticleSystem.MainModule-
startRotation.html) of 90 degrees when using
[ParticleSystem.ShapeModule.alignToDirection](ParticleSystem.ShapeModule-
alignToDirection.html), and all the particles become perpendicular to the
surface, like little spikes sticking out of it.

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool toggle = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var shape = ps.shape;
            shape.alignToDirection = toggle;
        }  
      
        void OnGUI()
        {
            toggle = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(25, 45, 200, 30), toggle, "[Align](UIElements.Align.html) To [Direction](UIElements.NavigationMoveEvent.Direction.html)");
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

