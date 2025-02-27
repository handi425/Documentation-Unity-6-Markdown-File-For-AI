[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/UnderstandingPerformanceStringsAndText.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceStringsAndText.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceStringsAndText.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceStringsAndText.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/UnderstandingPerformanceStringsAndText.html)
  * [中文](/cn/current/Manual/UnderstandingPerformanceStringsAndText.html)
  * [日本語](/ja/current/Manual/UnderstandingPerformanceStringsAndText.html)
  * [한국어](/kr/current/Manual/UnderstandingPerformanceStringsAndText.html)

  * [Optimization](analysis.html)
  * [Understanding optimization in Unity](UnderstandingPerformance.html)
  * Strings and text

[](UnderstandingPerformanceAssetAuditing.html)

Asset auditing

[](UnderstandingPerformanceResourcesFolder.html)

The Resources folder

# Strings and text

Handling strings and text is a common source of performance problems in Unity
projects. In C#, all strings are **immutable** You cannot change the contents
of an immutable (read-only) package. This is the opposite of **mutable**. Most
packages are immutable, including packages downloaded from the package
registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable). Any manipulation of a string
results in the allocation of a full new string. This is relatively expensive,
and repeated string concatenations can develop into performance problems when
performed on large strings, on large datasets, or in tight loops.

Further, as N string concatenations require the allocation of N–1 intermediate
strings, serial concatenations can also be a major cause of managed memory
pressure.

For cases where strings must be concatenated in tight loops or during each
frame, use a StringBuilder to perform the actual concatenation operations. The
StringBuilder instance can also be reused to further minimize unnecessary
memory allocation.

Microsoft maintains a list of best practices for working with strings in C#,
which can be found here on the MSDN website:
[msdn.microsoft.com](https://msdn.microsoft.com/en-
us/library/dd465121\(v=vs.110\).aspx).

## Locale coercion and ordinal comparisons

One of the core performance problems often found in string-related code is the
unintended use of the slow, default string APIs. These APIs were built for
business applications, and attempt to deal with handling strings from many
different cultural and linguistic rules with regards to the characters found
in text.

For example, the following example code returns true when run under the US-
English locale, but returns false for many European locales.

**Note** : As of Unity 5.3 and 5.4, Unity’s scripting runtimes always run
under the US English (en-US) locale:

    
    
        String.Equals("encyclopedia", “encyclopædia”);
    

For most Unity projects, this is entirely unnecessary. It’s roughly ten times
faster to use the ordinal comparison type, which compares strings in a manner
familiar to C and C++ programmers: by simply comparing each sequential byte of
the string, without regard for the character represented by that byte.

Switching to ordinal string comparison is as simple as supplying
`StringComparison.Ordinal` as the final argument to `String.Equals`:

    
    
    myString.Equals(otherString, StringComparison.Ordinal);
    
    

## Inefficient built-in string APIs

Beyond switching to ordinal comparisons, certain C# `String` APIs are known to
be extremely inefficient. Among these are `String.Format`, `String.StartsWith`
and `String.EndsWith`. `String.Format` is difficult to replace, but the
inefficient string comparison methods are trivially optimized away.

While Microsoft’s recommendation is to pass `StringComparison.Ordinal` into
any string comparison that doesn’t need to be adjusted for localization, Unity
benchmarks show that the impact of this is relatively minimal compared to a
custom implementation.

Method | Time (ms) for 100k short strings  
---|---  
`String.StartsWith`, default culture | 137  
`String.EndsWith`, default culture | 542  
`String.StartsWith`, ordinal | 115  
`String.EndsWith`, ordinal | 34  
Custom `StartsWith` replacement | 4.5  
Custom `EndsWith` replacement | 4.5  
  
Both `String.StartsWith` and `String.EndsWith` can be replaced with simple
hand-coded versions, similar to the example attached below.

    
    
        public static bool CustomEndsWith(this string a, string b)
        {
            int ap = a.Length - 1;
            int bp = b.Length - 1;
        
            while (ap >= 0 && bp >= 0 && a [ap] == b [bp])
            {
                ap--;
                bp--;
            }
        
            return (bp < 0);
        }
    
        public static bool CustomStartsWith(this string a, string b)
        {
            int aLen = a.Length;
            int bLen = b.Length;
        
            int ap = 0; int bp = 0;
        
            while (ap < aLen && bp < bLen && a [ap] == b [bp])
            {
                ap++;
                bp++;
            }
        
            return (bp == bLen);
        }
    
    

## Regular Expressions

While Regular Expressions are a powerful way to match and manipulate strings,
they can be extremely performance-intensive. Further, due to the C# library’s
implementation of Regular Expressions, even simple Boolean `IsMatch` queries
allocate large transient datastructures “under the hood.” This transient
managed memory churn should be deemed unacceptable, except during
initialization.

If regular expressions are necessary, it’s strongly recommended to not use the
static `Regex.Match` or `Regex.Replace` methods, which accept the regular
expression as a string parameter. These methods compile the regular expression
on-the-fly and don’t cache the generated object.

This example code is an innocuous one-liner.

    
    
    Regex.Match(myString, "foo");
    
    

However, each time it’s executed, it generates 5 kilobytes of garbage. A
simple refactoring can eliminate much of this garbage:

    
    
    var myRegExp = new Regex("foo");
    
    myRegExp.Match(myString);
    
    

In this example, each call to `myRegExp.Match` “only” results in 320 bytes of
garbage. While this is still expensive for a simple matching operation, it’s a
considerable improvement over the previous example.

Therefore, if the regular expressions are invariant string literals, it’s
considerably more efficient to precompile them by passing them as the first
parameter of the Regex object’s constructor. These precompiled Regexes should
then be reused.

## XML, JSON and other long-form text parsing

Parsing text is often one of the heaviest operations that occurs at loading
time. Sometimes, the time spent parsing text can outweigh the time spent
loading and instantiating Assets.

The reasons behind this depend on the specific parser used. C#’s built-in XML
parser is extremely flexible, but as a result, it’s not optimizable for
specific data layouts.

Many third-party parsers are built on reflection. While reflection is an
excellent choice during development (because it allows the parser to rapidly
adapt to changing data layouts), it’s notoriously slow.

Unity has introduced a partial solution with its built-in
[JSONUtility](../ScriptReference/JsonUtility.html) API, which provides an
interface to Unity’s serialization system that reads/emits JSON. In most
benchmarks, it’s faster than pure C# JSON parsers, but it has the same
limitations as other interfaces to Unity’s serialization system – it can’t
serialized many complex data types, such as Dictionaries, without additional
code.

**Note** : See the
[ISerializationCallbackReceiver](../ScriptReference/ISerializationCallbackReceiver.html)
interface for one way to add the additional processing necessary to convert
to/from complex data types during Unity’s serialization process.

When encountering performance problems that arise from textual data parsing,
consider three alternative resolutions.

### Option 1: Parse at build time

The best way to avoid the cost of text parsing is to entirely eliminate the
parsing of text at runtime. In general, this means “baking” the textual data
into a binary format via some sort of build step.

Most developers who opt for this route move their data to some sort of
ScriptableObject-derived class hierarchy and then distribute the data via
AssetBundles. For an excellent discussion of using ScriptableObjects, see
[Richard Fine’s Unite 2016 talk](https://www.youtube.com/watch?v=VBA1QCoEAX4)
on youtube.

This strategy offers the best possible performance, but is only suitable for
data that doesn’t need to be generated dynamically. it’s best suited for game
design parameters and other content.

### Option 2: Split and lazy load

A second possibility is to split up the data that must be parsed into smaller
chunks. Once split, the cost of parsing the data can be spread across several
frames. In the ideal case, identify the specific portions of the data that are
required to present the desired experience to the user and load only those
portions.

In a simple example: if the project were a platform game, it would not be
necessary to serialize data for all the levels together into one giant blob.
If the data were split into individual Assets for each level, and perhaps
segmented the levels into regions, the data could be parsed as the player
approached it.

While this sounds easy, in practice it requires a substantial investment in
tool code and may require data structures to be reorganized.

### Option 3: Threads

For data that’s parsed entirely into plain C# objects, and doesn’t require any
interaction with Unity APIs, it’s possible to move the parsing operations to
worker threads.

This option can be extremely powerful on platforms with a significant number
of cores. However, it requires careful programming to avoid creating deadlocks
and race conditions.

**Note** : iOS devices have at most 2 cores. Most Android devices have from 2
to 4. This technique is of more interest when building for standalone and
console build targets.

Projects that choose to implement threading use the built-in C#
[Thread](https://msdn.microsoft.com/en-
us/library/system.threading.thread\(v=vs.110\).aspx) and
[ThreadPool](https://msdn.microsoft.com/en-
us/library/system.threading.threadpool\(v=vs.110\).aspx) classes (see
[msdn.microsoft.com](https://msdn.microsoft.com/en-
us/library/system.threading.thread\(v=vs.110\).aspx)) to manage their worker
threads, along with the standard C# synchronization classes.

[](UnderstandingPerformanceAssetAuditing.html)

Asset auditing

[](UnderstandingPerformanceResourcesFolder.html)

The Resources folder

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

