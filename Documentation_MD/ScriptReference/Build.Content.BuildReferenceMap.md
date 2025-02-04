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

# BuildReferenceMap

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

Container for holding information about where objects will be serialized in a
build.

This class helps ensure that Object references can be correctly resolved in
the final built data.  
  
Note: this class and its members exist to provide low-level support for the
**Scriptable Build Pipeline** package. This is intended for internal use only;
use the [Scriptable Build Pipeline
package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html)
to implement a fully featured build pipeline. You can install this via the
[Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-
manager-ui@latest/index.html).

### Constructors

[BuildReferenceMap](Build.Content.BuildReferenceMap-ctor.html)| Default
constructor for an empty BuildReferenceMap.  
---|---  
  
### Public Methods

[AddMapping](Build.Content.BuildReferenceMap.AddMapping.html)| Adds a mapping
for a single Object to where it will be serialized out to the build.  
---|---  
[AddMappings](Build.Content.BuildReferenceMap.AddMappings.html)| Adds mappings
for a set of Objects to where they will be serialized out to the build.  
[Dispose](Build.Content.BuildReferenceMap.Dispose.html)| Dispose the
BuildReferenceMap destroying all internal state.  
[Equals](Build.Content.BuildReferenceMap.Equals.html)| Returns true if the
objects are equal.  
[FilterToSubset](Build.Content.BuildReferenceMap.FilterToSubset.html)| Filters
this BuildReferenceMap instance to remove references to any objects that are
not in the array of ObjectIdentifiers specified by objectIds.  
[GetHash128](Build.Content.BuildReferenceMap.GetHash128.html)| Gets the hash
for the BuildReferenceMap.  
[GetHashCode](Build.Content.BuildReferenceMap.GetHashCode.html)| Gets the hash
code for the BuildReferenceMap.  
[GetObjectData](Build.Content.BuildReferenceMap.GetObjectData.html)|
ISerializable method for serialization support outside of Unity's internal
serialization system.  
  
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

