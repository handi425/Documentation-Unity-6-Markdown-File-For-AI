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

# ObjectIdentifier

struct in UnityEditor.Build.Content

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

Struct that identifies a specific object project wide.

Note: this struct and its members exist to provide low-level support for the
**Scriptable Build Pipeline** package. This is intended for internal use only;
use the [Scriptable Build Pipeline
package](https://docs.unity3d.com/Packages/com.unity.scriptablebuildpipeline@latest/index.html)
to implement a fully featured build pipeline. You can install this via the
[Unity Package Manager](https://docs.unity3d.com/Packages/com.unity.package-
manager-ui@latest/index.html).

### Properties

[filePath](Build.Content.ObjectIdentifier-filePath.html)| The file path on
disk that contains this object. (Only used for objects not known by the
AssetDatabase).  
---|---  
[fileType](Build.Content.ObjectIdentifier-fileType.html)| Type of file that
contains this object.  
[guid](Build.Content.ObjectIdentifier-guid.html)| The specific asset that
contains this object.  
[localIdentifierInFile](Build.Content.ObjectIdentifier-
localIdentifierInFile.html)| The index of the object inside a serialized file.  
  
### Public Methods

[CompareTo](Build.Content.ObjectIdentifier.CompareTo.html)| Implements the
IComparable interface.  
---|---  
[Equals](Build.Content.ObjectIdentifier.Equals.html)| Returns true if the
objects are equal.  
[GetHashCode](Build.Content.ObjectIdentifier.GetHashCode.html)| Gets the hash
code for the ObjectIdentifier.  
[ToString](Build.Content.ObjectIdentifier.ToString.html)| Returns a nicely
formatted string for this ObjectIdentifier.  
  
### Static Methods

[ToInstanceID](Build.Content.ObjectIdentifier.ToInstanceID.html)| Tries to
return the InstanceID that represents this ObjectIdentifier.  
---|---  
[ToObject](Build.Content.ObjectIdentifier.ToObject.html)| Tries to find, load,
and return the Object that represents this ObjectIdentifier.  
[TryGetObjectIdentifier](Build.Content.ObjectIdentifier.TryGetObjectIdentifier.html)|
Tries to convert a persistent Object into an ObjectIdentifier.  
  
### Operators

[operator !=](Build.Content.ObjectIdentifier-operator_ne.html)| Returns true
if the ObjectIdentifiers are different.  
---|---  
[operator <](Build.Content.ObjectIdentifier-operator_lt.html)| Returns true if
the first ObjectIdentifier is less than the second ObjectIdentifier.  
[operator ==](Build.Content.ObjectIdentifier-operator_eq.html)| Returns true
if the ObjectIdentifiers are the same.  
[operator >](Build.Content.ObjectIdentifier-operator_gt.html)| Returns true if
the first ObjectIdentifier is greater than the second ObjectIdentifier.  
  
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

