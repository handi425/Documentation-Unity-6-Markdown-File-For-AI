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

#  [ParticleSystem.MainModule](ParticleSystem.MainModule.html).simulationSpace

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

public [ParticleSystemSimulationSpace](ParticleSystemSimulationSpace.html)
simulationSpace;

### Description

This selects the space in which to simulate particles. It can be either world
or local space.

Toggle between local and world space simulation using the following example:

    
    
    using UnityEngine;
    using System.Collections;  
      
    [[RequireComponent](RequireComponent.html)(typeof([ParticleSystem](ParticleSystem.html)))]
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public bool useLocal = true;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();
            var main = ps.main;
            useLocal = main.simulationSpace == [ParticleSystemSimulationSpace.Local](ParticleSystemSimulationSpace.Local.html);
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
            var main = ps.main;
            main.simulationSpace = useLocal ? [ParticleSystemSimulationSpace.Local](ParticleSystemSimulationSpace.Local.html) : [ParticleSystemSimulationSpace.World](ParticleSystemSimulationSpace.World.html);
        }  
      
        void OnGUI()
        {
            useLocal = [GUI.Toggle](GUI.Toggle.html)(new [Rect](Rect.html)(10, 60, 200, 30), useLocal, "Use Local Simulation [Space](Space.html)");
        }
    }
    

Simulate particles relative to an independent game object using the following
example:

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    public class ParticleSystemScript : [MonoBehaviour](MonoBehaviour.html)
    {
        private [ParticleSystem](ParticleSystem.html) ps;
        public [Transform](Transform.html) relativeTo;  
      
        void Start()
        {
            ps = GetComponent<[ParticleSystem](ParticleSystem.html)>();  
      
            var main = ps.main;
            main.simulationSpace = [ParticleSystemSimulationSpace.Custom](ParticleSystemSimulationSpace.Custom.html);
            main.customSimulationSpace = relativeTo;
        }  
      
        void [Update](PlayerLoop.Update.html)()
        {
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

