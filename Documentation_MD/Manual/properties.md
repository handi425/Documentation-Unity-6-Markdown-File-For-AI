[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/properties.html)
  * [中文](/cn/current/Manual/properties.html)
  * [日本語](/ja/current/Manual/properties.html)
  * [한국어](/kr/current/Manual/properties.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/properties.html)
  * [中文](/cn/current/Manual/properties.html)
  * [日本語](/ja/current/Manual/properties.html)
  * [한국어](/kr/current/Manual/properties.html)

  * [Scripting](scripting.html)
  * [Object-oriented development](object-oriented-development.html)
  * Adding functionality to objects at runtime

[](web-request-creating-download-handlers.html)

Creating DownloadHandlers

[](property-bags.html)

Property bags

# Adding functionality to objects at runtime

You can use the Unity Properties API to visit .Net objects at runtime. The
Properties API is in the `Unity.Properties` namespace and it uses a [visitor
design pattern](https://en.wikipedia.org/wiki/Visitor_pattern) to visit .Net
objects at runtime. The visitor pattern is a design pattern that allows you to
add new operations to an existing object structure without modifying the
structure itself. You can build various functionalities on top of the visitor
pattern, such as serialization, data migration, deep data comparisons, and
data binding.

Unity Properties allows you to use visitors on any given type. You can use the
Properties API to do the following:

  * Create data types compatible with the Properties API
  * Develop new property visitors and adapters for domain-specific use cases

Topic | Description  
---|---  
[Property bags](property-bags.html) | Understand the concept and performance considerations about property bags.  
[Property visitors](property-visitors.html) | Understand the concept and performance considerations about property visitors.  
[Property paths](property-paths.html) | Understand the concept and performance considerations about property paths.  
[Use `PropertyVisitor` to create a property visitor](property-visitors-PropertyVisitor.html) | Learn how to use the `PropertyVisitor` base class to create a property visitor from an example.  
[Use low-level APIs to create a property visitor](property-visitors-low-level-api.html) | Learn how to use the `IPropertyBagVisitor` and `IPropertyVisitor` interfaces to create a property visitor from an example.  
  
## Additional resources

  * [Serialization](https://docs.unity3d.com/Packages/com.unity.serialization@latest)
  * [Runtime data binding](UIE-runtime-binding.html)

[](web-request-creating-download-handlers.html)

Creating DownloadHandlers

[](property-bags.html)

Property bags

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

