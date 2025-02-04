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

# ProfilerCategory

struct in Unity.Profiling

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Use to specify category for instrumentation Profiler markers.

    
    
    using Unity.Profiling;  
      
    public class MySystemClass
    {
        static readonly [ProfilerMarker](Unity.Profiling.ProfilerMarker.html) s_SimulatePerfMarker = new [ProfilerMarker](Unity.Profiling.ProfilerMarker.html)([ProfilerCategory.Ai](Unity.Profiling.ProfilerCategory.Ai.html), "MySystem.Simulate");  
      
        public void UpdateLogic()
        {
            using (s_SimulatePerfMarker.Auto())
            {
                // ...
            }
        }
    }
    

Additional resources: [ProfilerMarker](Unity.Profiling.ProfilerMarker.html).

### Static Properties

[Ai](Unity.Profiling.ProfilerCategory.Ai.html)| AI and NavMesh Profiler
category.  
---|---  
[Animation](Unity.Profiling.ProfilerCategory.Animation.html)| Animation
Profiler category.  
[Audio](Unity.Profiling.ProfilerCategory.Audio.html)| Audio system Profiler
category.  
[FileIO](Unity.Profiling.ProfilerCategory.FileIO.html)| File IO Profiler
category.  
[Gui](Unity.Profiling.ProfilerCategory.Gui.html)| UI Profiler category.  
[Input](Unity.Profiling.ProfilerCategory.Input.html)| Input system Profiler
category.  
[Internal](Unity.Profiling.ProfilerCategory.Internal.html)| Internal Unity
systems Profiler category.  
[Lighting](Unity.Profiling.ProfilerCategory.Lighting.html)| Global
Illumination Profiler category.  
[Loading](Unity.Profiling.ProfilerCategory.Loading.html)| Loading system
Profiler category.  
[Memory](Unity.Profiling.ProfilerCategory.Memory.html)| Memory allocation
Profiler category.  
[Network](Unity.Profiling.ProfilerCategory.Network.html)| Networking system
Profiler category.  
[Particles](Unity.Profiling.ProfilerCategory.Particles.html)| Particle system
Profiler category.  
[Physics](Unity.Profiling.ProfilerCategory.Physics.html)| Physics system
Profiler category.  
[Physics2D](Unity.Profiling.ProfilerCategory.Physics2D.html)| The Physics 2D
system category for the Profiler.  
[Render](Unity.Profiling.ProfilerCategory.Render.html)| Rendering system
Profiler category.  
[Scripts](Unity.Profiling.ProfilerCategory.Scripts.html)| Generic C# code
Profiler category.  
[Video](Unity.Profiling.ProfilerCategory.Video.html)| Video system Profiler
category.  
[VirtualTexturing](Unity.Profiling.ProfilerCategory.VirtualTexturing.html)|
Virtual Texturing system Profiler category.  
[Vr](Unity.Profiling.ProfilerCategory.Vr.html)| VR systen Profiler category.  
  
### Properties

[Color](Unity.Profiling.ProfilerCategory.Color.html)| Gets Profiler category
color.  
---|---  
[Name](Unity.Profiling.ProfilerCategory.Name.html)| Gets Profiler category
name.  
  
### Constructors

[ProfilerCategory](Unity.Profiling.ProfilerCategory-ctor.html)| Use to
construct ProfilerCategory by category name.  
---|---  
  
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

