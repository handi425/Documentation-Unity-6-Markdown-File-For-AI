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

#  [Lightmapping](Experimental.Lightmapping.html).SetCustomBakeInputs

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

public static void SetCustomBakeInputs(Vector4[] inputData, int sampleCount);

## Declaration

public static void SetCustomBakeInputs(ReadOnlySpan<Vector4> inputData, int
sampleCount);

### Parameters

inputData | The positions (xyz) of the points for which the amount of sky visibility is calculated. The w component is an offset that will be applied to the ray originating at the position.  
---|---  
sampleCount | The number of samples on the upper hemisphere used to calculate the sky visibility.  
  
### Description

Set the custom bake inputs.

The custom bake calculates the amount of sky visible from the input sample
points. The value is computed by shooting rays on the upper hemisphere above
each point and the result is the fraction of samples that reach the sky in a
direct line from each position (accounting for transparency). Each ray is
offset by the value specified in the w component of the input. The result
value is a single floating point number and is stored in (xyz) and will be
unnormalized. The value can be normalized by dividing with the number of
samples used for the custom bake. The w component of the result represent the
fraction of samples that strike a backface and can be used to detect samples
that lie inside geometry (i.e. they will have a high w value). The data can be
used in a custom shader to account for sky visibility on objects that are
difficult to bake such as trees and foliage. This way points that lie within
the crown of a tree for example will become darker since fewer rays will
escape to the sky.

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

