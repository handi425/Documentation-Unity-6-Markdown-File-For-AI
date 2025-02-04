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

# RayTracingInstanceCullingConfig

struct in UnityEngine.Rendering

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

Parameters for culling and filtering ray tracing instances in
[RayTracingAccelerationStructure.CullInstances](Rendering.RayTracingAccelerationStructure.CullInstances.html).

Additional resources:
[RayTracingAccelerationStructure](Rendering.RayTracingAccelerationStructure.html).

### Properties

[alphaTestedMaterialConfig](Rendering.RayTracingInstanceCullingConfig-
alphaTestedMaterialConfig.html)| A configuration for defining when a Material
is considered being alpha tested.  
---|---  
[flags](Rendering.RayTracingInstanceCullingConfig-flags.html)| The flags that
control different options in RayTracingAccelerationStructure.CullInstances
function.  
[instanceTests](Rendering.RayTracingInstanceCullingConfig-instanceTests.html)|
An array of RayTracingInstanceCullingTest objects used add Renderers to the
acceleration structure based on their layer, ShadowCastingMode and Material
type.  
[lodParameters](Rendering.RayTracingInstanceCullingConfig-lodParameters.html)|
Parameters used for LOD culling.  
[materialTest](Rendering.RayTracingInstanceCullingConfig-materialTest.html)| A
Material-based test used in RayTracingAccelerationStructure.CullInstances.  
[minSolidAngle](Rendering.RayTracingInstanceCullingConfig-minSolidAngle.html)|
The minimum solid angle in degrees that Unity uses for culling ray tracing
instances associated with the Renderers in a Scene.  
[planes](Rendering.RayTracingInstanceCullingConfig-planes.html)| An array of
planes used for culling ray tracing instances associated with the Renderers in
a Scene.  
[sphereCenter](Rendering.RayTracingInstanceCullingConfig-sphereCenter.html)|
The center of the sphere used for culling ray tracing instances associated
with the Renderers in a Scene.  
[sphereRadius](Rendering.RayTracingInstanceCullingConfig-sphereRadius.html)|
The radius of the sphere used for culling ray tracing instances associated
with the Renderers in a Scene.  
[subMeshFlagsConfig](Rendering.RayTracingInstanceCullingConfig-
subMeshFlagsConfig.html)| The configuration that defines the
RayTracingSubMeshFlags values for different types of Materials.  
[transparentMaterialConfig](Rendering.RayTracingInstanceCullingConfig-
transparentMaterialConfig.html)| A configuration for defining when a Material
is considered being transparent.  
[triangleCullingConfig](Rendering.RayTracingInstanceCullingConfig-
triangleCullingConfig.html)| A structure used for specifying ray tracing
instance triangle culling options and vertex winding.  
  
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

