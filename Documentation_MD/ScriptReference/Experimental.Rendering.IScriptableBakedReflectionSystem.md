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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# IScriptableBakedReflectionSystem

interface in UnityEditor.Experimental.Rendering

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

Defines the required members for a ScriptableBakedReflectionSystem
implementation.

You can use the empty implementation as base class, see
[ScriptableBakedReflectionSystem](Experimental.Rendering.ScriptableBakedReflectionSystem.html).

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Rendering;
    using UnityEditor.Experimental.Rendering;  
      
    public interface IBakeJobs
    {
        // Add job counts + remove jobs count
        int count { get; }
        int toAddCount { get; }
        int toRemoveCount { get; }
    }  
      
    public interface IBaker<TProbe>
    {
        IBakeJobs PrepareBakeJobsFor([SceneStateHash](Experimental.Rendering.SceneStateHash.html) sceneStateHash);
        void IssueJobs(IBakeJobs jobs);
        List<TProbe> bakedProbes { get; set; }
        void StopRunningJobs();
    }  
      
    abstract class CustomScriptableBakedReflectionSystem : [ScriptableBakedReflectionSystem](Experimental.Rendering.ScriptableBakedReflectionSystem.html)
    {
        enum [Stage](SceneManagement.Stage.html)
        {
            None,
            BakeReflectionProbes
        }  
      
        IBaker<[ReflectionProbe](ReflectionProbe.html)> m_ReflectionProbeBaker;  
      
        public CustomScriptableBakedReflectionSystem(
            IBaker<[ReflectionProbe](ReflectionProbe.html)> reflectionProbeBaker)
        // Our custom system processes in 1 stage: reflection probes
            : base(1)
        {
            m_ReflectionProbeBaker = reflectionProbeBaker;
        }  
      
        public override void Tick(
            [SceneStateHash](Experimental.Rendering.SceneStateHash.html) sceneStateHash,
            [IScriptableBakedReflectionSystemStageNotifier](Experimental.Rendering.IScriptableBakedReflectionSystemStageNotifier.html) handle)
        {
            // Reflection Probes
            {
                // Calculate reflection probes to remove and to bake and add
                var jobs = m_ReflectionProbeBaker.PrepareBakeJobsFor(sceneStateHash);
                if (jobs.count > 0)
                {
                    // [Update](PlayerLoop.Update.html) progression information of current stage
                    // [Progress](Progress.html) is the progression of to bake and add jobs
                    handle.EnterStage(
                        (int)Stage.BakeReflectionProbes,
                        string.Format("Reflection Probes | {0} jobs", jobs.toAddCount),
                        1 - (jobs.toAddCount / (float)m_ReflectionProbeBaker.bakedProbes.Count));  
      
                    // Perform removal of remove jobs
                    // Issue baking of add jobs if they are not in progress
                    m_ReflectionProbeBaker.IssueJobs(jobs);  
      
                    return;
                }
                handle.ExitStage((int)Stage.BakeReflectionProbes);
            }  
      
            // [Update](PlayerLoop.Update.html) the hash of the reflection system
            stateHashes = CalculateStateHash();
            // Baking is complete for this sceneStateHash
            handle.SetIsDone(true);
        }  
      
        public override void SynchronizeReflectionProbes()
        {
            // Synchronize Reflection Probes
            for (int i = 0, c = m_ReflectionProbeBaker.bakedProbes.Count; i < c; ++i)
            {
                var probe = m_ReflectionProbeBaker.bakedProbes[i];
                probe.bakedTexture = GetReflectionProbeBakedTexture(probe);
            }
        }  
      
        public override void Clear()
        {
            m_ReflectionProbeBaker.bakedProbes.Clear();
            DeleteBakedReflectionProbeTextures();
        }  
      
        public override void Cancel()
        {
            m_ReflectionProbeBaker.StopRunningJobs();
        }  
      
        [Cubemap](Cubemap.html) GetReflectionProbeBakedTexture([ReflectionProbe](ReflectionProbe.html) probe)
        {
            throw new System.NotImplementedException();
        }  
      
        protected abstract void DeleteBakedReflectionProbeTextures();
        protected abstract [Hash128](Hash128.html)[] CalculateStateHash();
    }
    

### Properties

[stageCount](Experimental.Rendering.IScriptableBakedReflectionSystem-
stageCount.html)| Number of stages of the baking process.  
---|---  
[stateHashes](Experimental.Rendering.IScriptableBakedReflectionSystem-
stateHashes.html)| The hashes of the current baked state of the
ScriptableBakedReflectionSystem.  
  
### Public Methods

[BakeAllReflectionProbes](Experimental.Rendering.IScriptableBakedReflectionSystem.BakeAllReflectionProbes.html)|
Implement this method to bake all of the loaded reflection probes.  
---|---  
[Cancel](Experimental.Rendering.IScriptableBakedReflectionSystem.Cancel.html)|
Cancel the running bake jobs.  
[Clear](Experimental.Rendering.IScriptableBakedReflectionSystem.Clear.html)|
Clear the state of the ScriptableBakedReflectionSystem.  
[SynchronizeReflectionProbes](Experimental.Rendering.IScriptableBakedReflectionSystem.SynchronizeReflectionProbes.html)|
Synchronize the baked data with the actual components and rendering settings.  
[Tick](Experimental.Rendering.IScriptableBakedReflectionSystem.Tick.html)|
This method is called every Editor update until the
ScriptableBakedReflectionSystem indicates that the baking is complete, with
handle.SetIsDone(true). (See
IScriptableBakedReflectionSystemStageNotifier.SetIsDone).  
  
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

