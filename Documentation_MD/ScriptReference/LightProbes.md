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

# LightProbes

class in UnityEngine

/

Inherits from:[Object](Object.html)

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

Stores light probe data for all currently loaded Scenes.

The data includes: probe positions, Spherical Harmonics (SH) coefficients and
the tetrahedral tessellation.  
  
You can modify the probe positions and coefficients, and update the
tetrahedral tessellation at runtime. You can also swap the entire
`LightProbes` object for a different pre-baked one using
[LightmapSettings.lightProbes](LightmapSettings-lightProbes.html).  
  
To retrieve the `LightProbes` objects for a specific scene, use
[LightProbes.GetInstantiatedLightProbesForScene](LightProbes.GetInstantiatedLightProbesForScene.html)
or
[LightProbes.GetSharedLightProbesForScene](LightProbes.GetSharedLightProbesForScene.html).  
  
Additional resources: [Light Probes in the Unity
Manual](../Manual/LightProbes.html),
[LightmapSettings](LightmapSettings.html), [ReceiveGI](ReceiveGI.html).

### Properties

[bakedProbes](LightProbes-bakedProbes.html)| Coefficients of baked light
probes.  
---|---  
[cellCount](LightProbes-cellCount.html)| The number of cells space is divided
into (Read Only).  
[cellCountSelf](LightProbes-cellCountSelf.html)| The number of cells space is
divided into for this LightProbes object (Read Only).  
[count](LightProbes-count.html)| The number of light probes (Read Only).  
[countSelf](LightProbes-countSelf.html)| The number of light probes stored in
this LightProbes object (Read Only).  
[positions](LightProbes-positions.html)| Positions of the baked light probes
(Read Only).  
  
### Public Methods

[GetPositionsSelf](LightProbes.GetPositionsSelf.html)| Gets the positions of
the baked light probes stored in this LightProbes object.  
---|---  
[SetPositionsSelf](LightProbes.SetPositionsSelf.html)| Sets the positions of
the baked light probes stored in this LightProbes object.  
  
### Static Methods

[CalculateInterpolatedLightAndOcclusionProbes](LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html)|
Calculate light probes and occlusion probes at the given world space
positions.  
---|---  
[GetInstantiatedLightProbesForScene](LightProbes.GetInstantiatedLightProbesForScene.html)|
Gets an instantiated clone of the LightProbes object for a specific scene.  
[GetInterpolatedProbe](LightProbes.GetInterpolatedProbe.html)| Returns an
interpolated probe for the given position for both real-time and baked light
probes combined.  
[GetSharedLightProbesForScene](LightProbes.GetSharedLightProbesForScene.html)|
Gets the shared LightProbes object for a specific scene.  
[Tetrahedralize](LightProbes.Tetrahedralize.html)| Synchronously
tetrahedralize the currently loaded LightProbe positions.  
[TetrahedralizeAsync](LightProbes.TetrahedralizeAsync.html)| Asynchronously
tetrahedralize all currently loaded LightProbe positions.  
  
### Events

[lightProbesUpdated](LightProbes-lightProbesUpdated.html)| Unity raises this
event to indicate that the light probe structure (tetrahedralization) or
values (spherical harmonics coefficients) have changed.  
---|---  
[needsRetetrahedralization](LightProbes-needsRetetrahedralization.html)| An
event which is called when the number of currently loaded light probes changes
due to additive scene loading or unloading.  
[tetrahedralizationCompleted](LightProbes-tetrahedralizationCompleted.html)|
Event which is called after LightProbes.Tetrahedralize or
LightProbes.TetrahedralizeAsync has finished computing a tetrahedralization.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

