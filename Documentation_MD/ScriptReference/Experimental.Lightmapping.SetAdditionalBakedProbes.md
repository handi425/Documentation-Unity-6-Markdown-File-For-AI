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

#  [Lightmapping](Experimental.Lightmapping.html).SetAdditionalBakedProbes

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

**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.

## Declaration

public static void SetAdditionalBakedProbes(int id, Vector3[] positions);

**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.

## Declaration

public static void SetAdditionalBakedProbes(int id, ReadOnlySpan<Vector3>
positions);

**Obsolete** Please use UnityEngine.LightTransport.IProbeIntegrator instead.

## Declaration

public static void SetAdditionalBakedProbes(int id, ReadOnlySpan<Vector3>
positions, bool dering);

### Parameters

id | An ID to identify the positions to be baked. This ID is used later to retrieve the result for those positions.  
---|---  
positions | An array of probe positions.  
dering | A boolean that determines if Unity should remove ringing from probes.  
  
### Description

Submit additional probe positions to be baked using an identifier.

Additional baked probes are probes that can be baked independently of any
Light Probe Groups. The baked probe data contains spherical harmonic L2
coefficients as well as a single float value to determine the validity of each
probe. By setting an array of probe positions with an identifier, a successive
bake will produce probe results for these positions, which can then be fetched
again from the API using the identifier.

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

