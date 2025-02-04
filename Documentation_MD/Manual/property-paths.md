[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/property-paths.html)
  * [中文](/cn/current/Manual/property-paths.html)
  * [日本語](/ja/current/Manual/property-paths.html)
  * [한국어](/kr/current/Manual/property-paths.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/property-paths.html)
  * [中文](/cn/current/Manual/property-paths.html)
  * [日本語](/ja/current/Manual/property-paths.html)
  * [한국어](/kr/current/Manual/property-paths.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * [Adding functionality to objects at runtime](properties.html)
  * Property paths

[](property-visitors.html)

Property visitors

[](property-visitors-propertyvisitor.html)

Use PropertyVisitor to create a property visitor

# Property paths

Property paths are strings that describe the location of a property within a
container object.

## Concept

You can use property paths to get or set the data of an object at a specific
path or accept a visitor on a sub-property of an object.

Property paths are constructed from strings and resolve a specific property
instance from a root object. For example, the path `foo.bar.baz[12]` resolves
the 13th element of the `baz` list container within the `bar` container, which
is nested inside the `foo` container.

To create and manipulate property paths, use the
[`Unity.Properties.PropertyPath`](../ScriptReference/Unity.Properties.PropertyPath.html)
class.

You can use property paths to do the following:

  * Get or set the data of an object at a specific path
  * Accept a visitor on a sub-property of an object

## Performance considerations

[`Unity.Properties.PropertyPath`](../ScriptReference/Unity.Properties.PropertyPath.html)
is an **immutable** You cannot change the contents of an immutable (read-only)
package. This is the opposite of **mutable**. Most packages are immutable,
including packages downloaded from the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable) struct type. When you construct a
property path from a string, allocations occur for sub-string extraction.

The following table lists the allocation behaviors when a property path is
constructed from a string:

String | Length | Allocations | Allocations reason  
---|---|---|---  
`"Path"` | 1 | 0 | Use the string as-is.  
`"Path.To"` | 2 | 2 | Split the string into two parts.  
`"Path.To[2]"` | 3 | 3 | Split the string into two parts and extract the index.  
`"Path.To[2].My"` | 4 | 4 |   
`"Path.To[2].My.Value"` | 5 | 6 | Allocate an array for the additional parts.  
  
The following table lists the allocation behaviors when a property path is
constructed from parts:

String | Length | Allocations | Allocations reason  
---|---|---|---  
`PropertyPath.FromName("Path")` | 1 | 0 |   
`PropertyPath.AppendName(previous, "To")` | 2 | 0 |   
`PropertyPath.AppendIndex(previous, 2)` | 3 | 0 |   
`PropertyPath.AppendName(previous, "My")` | 4 | 0 |   
`PropertyPath.AppendName(previous, "Value")` | 5 | 1 | Allocate an array for the additional parts.  
  
To optimize performance and avoid allocating memory:

  * Initialize and cache property paths during initialization routines.
  * Combine or append property path parts instead of constructing it from a string, up to four parts.

## Additional resources

  * [Property bags](property-bags.html)
  * [Property visitors](property-visitors.html)
  * [Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html)
  * [Use low-level APIs to create a property visitor](property-visitors-low-level-api.html)

[](property-visitors.html)

Property visitors

[](property-visitors-propertyvisitor.html)

Use PropertyVisitor to create a property visitor

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

