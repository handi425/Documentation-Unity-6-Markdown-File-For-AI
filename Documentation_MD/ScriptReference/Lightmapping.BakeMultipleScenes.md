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

#  [Lightmapping](Lightmapping.html).BakeMultipleScenes

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

public static void BakeMultipleScenes(string[] paths);

### Parameters

paths | The path of the Scenes that should be baked.  
---|---  
  
### Description

Bakes an array of Scenes.

This loads all Scenes and then builds all lightmaps, Reflection Probes and
Enlighten Realtime Global Illumination data. The function automatically splits
baked data by Scene. This means you can bake lightmaps for two adjacent levels
and have light and shadows cast onto objects in level A affect objects in
level B.  
  
Enlighten system data automatically connects neighboring systems when it is
additively loaded, thus bounce lighting can flow from one Scene to another.  
  
A single LightProbe asset is generated for all Scenes. Hence for the time
being, lightprobes always take as much memory as there are lightprobes in all
levels that are baked together.  
  
Only one ambient probe & default sky probe will be baked and assigned to each
Scene.  
  
Multiple Lightmapsnapshot objects containing the data for each Scene are
written into a single file in "MyScene/LightmapSnapshot.asset". At build time
this data will also be automatically split as well, hence if you bake multiple
Scenes but then only deploy one Scene then only the lightmap data for that
Scene will be deployed.

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

