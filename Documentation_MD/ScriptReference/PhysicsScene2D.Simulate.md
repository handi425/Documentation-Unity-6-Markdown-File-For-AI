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

#  [PhysicsScene2D](PhysicsScene2D.html).Simulate

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

public bool Simulate(float deltaTime, int simulationLayers =
Physics2D.AllLayers);

### Parameters

deltaTime | The time to advance physics by.  
---|---  
simulationLayers | The [Rigidbody2D](Rigidbody2D.html) and [Collider2D](Collider2D.html) layers to simulate.  
  
### Returns

**bool** Whether the simulation was run or not. Running the simulation during
physics callbacks will always fail.

### Description

Simulate physics associated with this [PhysicsScene](PhysicsScene.html).

Calling [PhysicsScene2D.Simulate](PhysicsScene2D.Simulate.html) will perform a
single simulation step, simulating physics over the specified `step` time.  
  
By default, [All Layers](Physics2D.AllLayers.html) are simulated, however if
you specify layers then only the [Rigidbody2D](Rigidbody2D.html) will be
simulated. Along with this, only contacts for [Collider2D](Collider2D.html) on
the specified layer(s) will be handled. Finally, only [joints](Joint2D.html)
or [effectors](Effector2D.html) on the specified layer(s) will be handled.  
  
You can call [PhysicsScene2D.Simulate](PhysicsScene2D.Simulate.html) in the
Editor outside of play mode, however caution is advised as this will cause the
simulation to move GameObjects that have an attached
[Rigidbody2D](Rigidbody2D.html) component. When simulating in the Editor
outside of play mode, a full simulation occurs for all physics components
including [Rigidbody2D](Rigidbody2D.html), [Collider2D](Collider2D.html),
[Joint2D](Joint2D.html) and [Effector2D](Effector2D.html), and contacts are
generated. However, contacts are not reported via the standard script
callbacks. This is a safety measure to prevent callbacks from deleting objects
in the Scene, which is not an undoable operation.  
  
**NOTE:** Calling [Physics2D.Simulate](Physics2D.Simulate.html) does not cause
Unity to call FixedUpdate. Unity still calls
[MonoBehaviour.FixedUpdate](MonoBehaviour.FixedUpdate.html) at the rate
defined by [Time.fixedDeltaTime](Time-fixedDeltaTime.html) whether automatic
simulation is on or off, and regardless of when you call Physics2D.Simulate.
Also, if you pass framerate-dependent step values (such as
[Time.deltaTime](Time-deltaTime.html)) to the physics engine, your simulation
will be less deterministic because of the unpredictable fluctuations in
framerate that can arise. To achieve more deterministic physics results, you
should pass a fixed step value to Physics2D.Simulate every time you call it.  
  
Additional resources:
[Physics2D.simulationMode](Physics2D-simulationMode.html) and
[Physics2D.Simulate](Physics2D.Simulate.html).  
  
Here is an example of a basic simulation that implements what's being done in
the automatic simulation mode.

    
    
    using UnityEngine;  
      
    public class BasicSimulation : [MonoBehaviour](MonoBehaviour.html)
    {
        public [PhysicsScene](PhysicsScene.html) physicsScene;
        private float timer;  
      
        void [Update](PlayerLoop.Update.html)()
        {
            if (!physicsScene.IsValid())
                return; // do nothing if the physics [Scene](SceneManagement.Scene.html) is not valid.  
      
            timer += [Time.deltaTime](Time-deltaTime.html);  
      
            // Catch up with the game time.
            // Advance the physics simulation in portions of [Time.fixedDeltaTime](Time-fixedDeltaTime.html)
            // Note that generally, we don't want to pass variable delta to Simulate as that leads to unstable results.
            while (timer >= [Time.fixedDeltaTime](Time-fixedDeltaTime.html))
            {
                timer -= [Time.fixedDeltaTime](Time-fixedDeltaTime.html);
                physicsScene.Simulate([Time.fixedDeltaTime](Time-fixedDeltaTime.html));
            }  
      
            // Here you can access the transforms state right after the simulation, if needed...
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

