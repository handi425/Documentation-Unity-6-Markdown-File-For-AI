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

# BuildUsageTagSet

class in UnityEditor.Build.Content

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

Container for holding information about how objects are being used in a build.

This class helps ensure the correct Shared Variants, Mesh Channels, and more
are included in the build correctly.  
  
Note: this class and its members exist to provide low-level support for the
**Scriptable Build Pipeline** package. This is intended for internal use only;
use the [Scriptable Build Pipeline
package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html)
to implement a fully featured build pipeline. You can install this via the
[Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-
manager-ui@latest/index.html).

### Constructors

[BuildUsageTagSet](Build.Content.BuildUsageTagSet-ctor.html)| Default
constructor for an empty BuildUsageTagSet.  
---|---  
  
### Public Methods

[Dispose](Build.Content.BuildUsageTagSet.Dispose.html)| Dispose the
BuildUsageTagSet destroying all internal state.  
---|---  
[Equals](Build.Content.BuildUsageTagSet.Equals.html)| Returns true if the
objects are equal.  
[FilterToSubset](Build.Content.BuildUsageTagSet.FilterToSubset.html)| Filters
this BuildUsageTagSet instance to remove references to any objects that are
not in the array of ObjectIdentifiers specified by objectIds.  
[GetHash128](Build.Content.BuildUsageTagSet.GetHash128.html)| Gets the hash
for the BuildReferenceMap.  
[GetHashCode](Build.Content.BuildUsageTagSet.GetHashCode.html)| Gets the hash
code for the BuildUsageTagSet.  
[GetObjectData](Build.Content.BuildUsageTagSet.GetObjectData.html)|
ISerializable method for serialization support outside of Unity's internal
serialization system.  
[GetObjectIdentifiers](Build.Content.BuildUsageTagSet.GetObjectIdentifiers.html)|
Returns an array of ObjectIdentifiers that this BuildUsageTagSet contains
usage information about.  
[UnionWith](Build.Content.BuildUsageTagSet.UnionWith.html)| Adds the Object
usage information from another BuildUsageTagSet to this BuildUsageTagSet.  
  
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

