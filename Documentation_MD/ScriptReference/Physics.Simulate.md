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

#  [Physics](Physics.html).Simulate

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

public static void Simulate(float step);

### Parameters

step | The time to advance physics by.  
---|---  
  
### Description

Simulate physics in the Scene.

Call this to simulate physics manually when the simulation mode is set to
Script. Simulation includes all the stages of collision detection, rigidbody
and joints integration, and filing of the physics callbacks (contact, trigger
and joints). Calling Physics.Simulate does not cause FixedUpdate to be called.
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) will still be
called at the rate defined by [Time.fixedDeltaTime](Time-fixedDeltaTime.html)
whether simulation mode is set to Script or not, and regardless of when you
call Physics.Simulate.  
  
Note that if you pass framerate-dependent step values (such as
[Time.deltaTime](Time-deltaTime.html)) to the physics engine, your simulation
will be non-deterministic because of the unpredictable fluctuations in
framerate that can arise.  
  
To achieve deterministic physics results, you should pass a fixed step value
to Physics.Simulate every time you call it. Usually, `step` should be a small
positive number. Using `step` values greater than 0.03 is likely to produce
inaccurate results.  
  
Additional resources: [Physics.simulationMode](Physics-simulationMode.html),
[SimulationMode](SimulationMode.html).  
  
Here is an example of a basic simulation that implements what's being done in
the [SimulationMode.FixedUpdate](SimulationMode.FixedUpdate.html) simulation
mode (excluding [Time.maximumDeltaTime](Time-maximumDeltaTime.html)).

    
    
    using UnityEngine;  
      
    public class BasicSimulation : [MonoBehaviour](MonoBehaviour.html)
    {
        private float timer;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if ([Physics.simulationMode](Physics-simulationMode.html) != [SimulationMode.Script](SimulationMode.Script.html))
                return; // do nothing if the automatic simulation is enabled  
      
            timer += [Time.deltaTime](Time-deltaTime.html);  
      
            // Catch up with the game time.
            // Advance the physics simulation in portions of [Time.fixedDeltaTime](Time-fixedDeltaTime.html)
            // Note that generally, we don't want to pass variable delta to Simulate as that leads to unstable results.
            while (timer >= [Time.fixedDeltaTime](Time-fixedDeltaTime.html))
            {
                timer -= [Time.fixedDeltaTime](Time-fixedDeltaTime.html);
                [Physics.Simulate](Physics.Simulate.html)([Time.fixedDeltaTime](Time-fixedDeltaTime.html));
            }  
      
            // Here you can access the transforms state right after the simulation, if needed
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

