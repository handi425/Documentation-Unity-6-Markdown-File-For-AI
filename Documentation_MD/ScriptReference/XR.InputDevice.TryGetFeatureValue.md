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

#  [InputDevice](XR.InputDevice.html).TryGetFeatureValue

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

public bool TryGetFeatureValue(InputFeatureUsage<bool> usage, out bool value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<uint> usage, out uint value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<float> usage, out float
value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Vector2> usage, out
[Vector2](Vector2.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Vector3> usage, out
[Vector3](Vector3.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Quaternion> usage, out
[Quaternion](Quaternion.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Bone> usage, out
[XR.Bone](XR.Bone.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Hand> usage, out
[XR.Hand](XR.Hand.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Eyes> usage, out
[XR.Eyes](XR.Eyes.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<InputTrackingState> usage,
out [XR.InputTrackingState](XR.InputTrackingState.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<bool> usage, DateTime time,
out bool value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<uint> usage, DateTime time,
out uint value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<float> usage, DateTime time,
out float value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Vector2> usage, DateTime
time, out [Vector2](Vector2.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Vector3> usage, DateTime
time, out [Vector3](Vector3.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<Quaternion> usage, DateTime
time, out [Quaternion](Quaternion.html) value);

## Declaration

public bool TryGetFeatureValue(InputFeatureUsage<InputTrackingState> usage,
DateTime time, out [XR.InputTrackingState](XR.InputTrackingState.html) value);

### Parameters

usage | Usage that describes the feature to retrieve.  
---|---  
time | A DateTime struct with the local time at which to query for data.  
value | A variable of the appropriate type to receive the information about the feature.  
  
### Returns

**bool** True if the feature information is retrieved; otherwise false.

### Description

Retrieves information about the input feature specified by the Usage
parameter. Those functions which take a time parameter allow querying for that
feature at a particular point in time

See XR.InputDevice.CommonUsages for valid usages that can be used to retrieve
input values. Note: not all of these features will be available on all
devices. If a feature is not available this function will return false.

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

