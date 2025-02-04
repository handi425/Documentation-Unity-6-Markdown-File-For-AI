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

# VFXSpawnerState

class in UnityEngine.VFX

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

### Description

The spawn state of a Spawn system.

This class is useful for debugging a Visual Effect's spawner. For example, you
can see if the effect is currently playing, the number of loops the spawner
has processed, as well as the current [state](VFX.VFXSpawnerLoopState.html) of
the spawner.  
  
To access the state of a Visual Effect's Spawn system, either use
[VisualEffect.GetSpawnSystemInfo](VFX.VisualEffect.GetSpawnSystemInfo.html)
or, in a class that inherits from
[VFXSpawnerCallbacks](VFX.VFXSpawnerCallbacks.html), override the
[OnUpdate](VFX.VFXSpawnerCallbacks.OnUpdate.html) method.

    
    
    using UnityEngine;
    using UnityEngine.VFX;  
      
    class ConstantRateEquivalent : [VFXSpawnerCallbacks](VFX.VFXSpawnerCallbacks.html)
    {
        public class InputProperties
        {
            [Min(0), Tooltip("Sets the number of particles to spawn per second.")]
            public float Rate = 10;
        }  
      
        static private readonly int rateID = [Shader.PropertyToID](Shader.PropertyToID.html)("Rate");  
      
        public sealed override void OnPlay([VFXSpawnerState](VFX.VFXSpawnerState.html) state, [VFXExpressionValues](VFX.VFXExpressionValues.html) vfxValues, [VisualEffect](VFX.VisualEffect.html) vfxComponent)
        {
        }  
      
        public sealed override void OnUpdate([VFXSpawnerState](VFX.VFXSpawnerState.html) state, [VFXExpressionValues](VFX.VFXExpressionValues.html) vfxValues, [VisualEffect](VFX.VisualEffect.html) vfxComponent)
        {
            if (state.playing)
            {
                float currentRate = vfxValues.GetFloat(rateID);
                state.spawnCount += currentRate * state.deltaTime;
            }
        }  
      
        public sealed override void OnStop([VFXSpawnerState](VFX.VFXSpawnerState.html) state, [VFXExpressionValues](VFX.VFXExpressionValues.html) vfxValues, [VisualEffect](VFX.VisualEffect.html) vfxComponent)
        {
        }
    }
    

### Properties

[delayAfterLoop](VFX.VFXSpawnerState-delayAfterLoop.html)| The current delay
time that the VFXSpawner waits for after it finishes a loop.  
---|---  
[delayBeforeLoop](VFX.VFXSpawnerState-delayBeforeLoop.html)| The current delay
time that the VFXSpawner waits for before it starts a loop.  
[deltaTime](VFX.VFXSpawnerState-deltaTime.html)| The current delta time.  
[loopCount](VFX.VFXSpawnerState-loopCount.html)| The current loop count.  
[loopDuration](VFX.VFXSpawnerState-loopDuration.html)| The duration of the
looping state.  
[loopIndex](VFX.VFXSpawnerState-loopIndex.html)| The current index of loop.  
[loopState](VFX.VFXSpawnerState-loopState.html)| The current state of
VFXSpawnerState.  
[newLoop](VFX.VFXSpawnerState-newLoop.html)| This boolean indicates if a new
loop has just started.  
[playing](VFX.VFXSpawnerState-playing.html)| The current playing state.  
[spawnCount](VFX.VFXSpawnerState-spawnCount.html)| The current Spawn count.  
[totalTime](VFX.VFXSpawnerState-totalTime.html)| The accumulated delta time
since the last Play event.  
[vfxEventAttribute](VFX.VFXSpawnerState-vfxEventAttribute.html)| Gets the
modifiable current event attribute (Read Only).  
  
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

