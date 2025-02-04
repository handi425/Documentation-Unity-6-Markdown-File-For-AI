[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceGeneralOptimizations.html)

  * [Optimization](analysis.html)
  * [Understanding optimization in Unity](UnderstandingPerformance.html)
  * General Optimizations

[](UnderstandingPerformanceResourcesFolder.html)

The Resources folder

[](UnderstandingPerformanceSpecialOptimizations.html)

Special optimizations

# General Optimizations

There are as many different ways to optimize code as there are reasons for
performance problems. In general, it is strongly recommended that developers
closely profile their applications before attempting to apply CPU
optimizations. However, there are several simple CPU optimizations that are
universally applicable.

## Address Properties by ID

Unity does not use string names to address Animator, Material and **Shader** A
program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) properties internally. For speed, all
property names are hashed into property IDs, and it is these IDs that are
actually used to address the properties.

Therefore, whenever using a _Set_ or _Get_ method on an Animator, Material or
Shader, use the integer-valued method instead of the string-valued methods.
The string methods simply perform string hashing and then forward the hashed
ID to the integer-valued methods.

The property IDs created from string hashes are deterministic over the course
of a single run. The simplest way to use them is to declare a static read-only
integer variable for each property name, and use the integer variable in place
of the string. These are automatically initialized during startup with no
further initialization code needed.

The appropriate APIs are
[Animator.StringToHash](../ScriptReference/Animator.StringToHash.html) for
Animator property names, and
[Shader.PropertyToID](../ScriptReference/Shader.PropertyToID.html) for
Material & Shader property names.

## Use non-allocating physics APIs

In Unity 5.3 and onwards, non-allocating versions of all Physics query APIs
have been introduced. Replace
[RaycastAll](../ScriptReference/Physics.RaycastAll.html) calls with
[RaycastNonAlloc](../ScriptReference/Physics.RaycastNonAlloc.html),
[SphereCastAll](../ScriptReference/Physics.SphereCastAll.html) calls with
[SphereCastNonAlloc](../ScriptReference/Physics.SphereCastNonAlloc.html), and
so on. For 2D applications, there are also non-allocating versions of all
Physics2D query APIs.

## Null comparisons against UnityEngine.Object subclasses

The Mono and **IL2CPP** A Unity-developed scripting back-end which you can use
as an alternative to Mono when building projects for some platforms. [More
info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) runtimes treat instances of classes
that derive from [UnityEngine.Object](../ScriptReference/Object.html) in a
specific way. Invoking methods on the instances actually calls into engine
code, which must perform lookups and validations to convert the script
references to the native references. While small, the cost of comparing a
variable of this type to null is much more expensive than a comparison against
a purely C# class. For this reason, avoid these null comparisons in tight
loops or in code that runs every frame.

### Vector and quaternion math and order of operations

For vector and **quaternion** Unity’s standard way of representing rotations
as data. When writing code that deals with rotations, you should usually use
the Quaternion class and its methods. [More
info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) math that is located in tight
loops, remember that integer math is faster than floating-point math, and
floating-point math is faster than vector, matrix or quaternion math.

Therefore, whenever commutative or associative arithmetic allows, attempt to
minimize the cost of individual mathematical operations:

    
    
    Vector3 x;
    
    int a, b;
    
    // Less efficient: results in two vector multiplications
    
    Vector3 slow = a * x * b;
    
    // More efficient: one integer mult, one vector mult
    
    Vector3 fast = a * b * x;
    
    

## Built-In ColorUtility

It is common for applications that must convert between HTML-formatted color
strings (`#RRGGBBAA`) and Unity’s native `Color` and `Color32` structures to
use a script from the Unify Community. This script was both slow and caused
extensive memory allocation due to string manipulation.

As of Unity 5, there is a built-in
[ColorUtility](../ScriptReference/ColorUtility.html) API that performs these
conversions efficiently. Usage of the built-in API should be preferred.

## Find and FindObjectOfType

It is a general best practice to eliminate all usage of
[`GameObject.Find`](../ScriptReference/GameObject.Find.html) and
[`Object.FindObjectOfType`](../ScriptReference/Object.FindObjectOfType.html)
in production code. As these APIs require Unity to iterate over all
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and Components in memory, they
rapidly become non-performant as the scope of a project grows.

An exception to the above rule can be made in accessors for singleton objects.
A global manager object often exposes an “instance” property, and often has a
`FindObjectOfType` call in the getter to detect pre-existing instances of the
singleton:

    
    
    class SomeSingleton {
    
        private SomeSingleton _instance;
    
        public SomeSingleton Instance {
    
            get {
    
                if(_instance == null) { 
    
                    _instance =
    
                        FindObjectOfType<SomeSingleton>(); 
    
                }
    
                if(_instance == null) { 
    
                    _instance = CreateSomeSingleton();
    
                }
    
                return _instance;
    
            }
    
        }
    
    }
    
    

While this pattern is generally acceptable, it is important to examine the
code and ensure that the accessor is be called in **Scenes** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) where the singleton object does not
exist. If the getter does not automatically create an instance of a missing
singleton, it is very common to discover that code looking for the singleton
results in repeated calls to `FindObjectOfType` (often multiple times per
frame) and creates an undesirable drain on performance.

## Debug code & the [conditional] attribute

The [`UnityEngine.Debug`](../ScriptReference/Debug.html) logging APIs are not
stripped from non-development builds, and do write to log files if called. As
most developers do not intend to write debug information in non-development
builds, it is recommended to wrap development-only logging calls in custom
methods, like so:

    
    
        public static class Logger {
    
            [Conditional("ENABLE_LOGS")]
    
            public static void Debug(string logMsg) {
    
                UnityEngine.Debug.Log(logMsg);
    
            }
    
        }
    
    

By decorating these methods with the [Conditional] attribute, the define or
defines used by the Conditional attribute determine whether the decorated
method is included in the compiled source.

If none of the defines passed to the Conditional attribute are defined, then
the decorated method _and_ all calls to the decorated method are compiled out.
The effect is identical to what would happen if the method and all calls to
the method were wrapped in `#if … #endif` preprocessor blocks.

For more information on the `Conditional` attribute, see the MSDN website:
[msdn.microsoft.com](https://msdn.microsoft.com/en-
us/library/4xssyw96\(v=vs.90\).aspx).

[](UnderstandingPerformanceResourcesFolder.html)

The Resources folder

[](UnderstandingPerformanceSpecialOptimizations.html)

Special optimizations

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

