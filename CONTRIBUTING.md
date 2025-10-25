# Contributing to AI Agent Context

Thank you for your interest in improving the AI agent context for this repository!

## Overview

This repository demonstrates best practices for configuring AI agent context with GitHub Copilot. Contributions that improve the clarity, accuracy, or usefulness of the context files are welcome.

## How to Contribute

### Improving Context Files

If you notice that Copilot suggestions don't align with project patterns, or you have ideas to improve the context:

1. **Identify the Issue**
   - Document specific cases where context could be improved
   - Note what Copilot suggested vs. what would be more appropriate
   - Consider if the issue is lack of context or unclear instructions

2. **Propose Changes**
   - Open an issue describing the improvement
   - Provide examples of desired behavior
   - Suggest specific wording or examples

3. **Submit a Pull Request**
   - Update the relevant context file(s)
   - Provide clear commit messages
   - Explain the rationale in your PR description
   - Include before/after examples if applicable

### What to Update

#### `.github/copilot-instructions.md`
Update this file when:
- Project patterns or conventions change
- New architectural decisions are made
- Team adopts new tools or frameworks
- Security or performance requirements evolve

#### `.github/AI-AGENT-CONTEXT-SPEC.md`
Update this file when:
- Best practices for AI context change
- New use cases are discovered
- Documentation structure improves
- Additional examples would help

#### `.github/QUICK-REFERENCE.md`
Update this file when:
- Common questions arise
- Workflow patterns change
- Tips or tricks are discovered

#### `.github/copilot-instructions.template.md`
Update this file when:
- Template structure can be improved
- Additional sections would help users
- Examples can be more comprehensive

## Guidelines for Context Updates

### Do:
✅ Test changes with actual Copilot usage
✅ Keep instructions clear and concise
✅ Provide specific, actionable guidance
✅ Include examples where helpful
✅ Consider the audience (developers using this project)
✅ Maintain consistent formatting and structure

### Don't:
❌ Add generic programming advice
❌ Include sensitive or confidential information
❌ Make instructions overly verbose
❌ Provide conflicting guidance
❌ Assume readers have specific knowledge

## Testing Your Changes

Before submitting a PR:

1. **Try it with Copilot**
   - Use Copilot with your updated context
   - Generate code in various scenarios
   - Check if suggestions improve

2. **Review for Clarity**
   - Read your changes from a new contributor's perspective
   - Ensure instructions are unambiguous
   - Check that examples are accurate

3. **Check Consistency**
   - Verify your changes don't conflict with other parts
   - Maintain the existing tone and style
   - Ensure formatting is consistent

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-context-xyz`)
3. Make your changes
4. Test with Copilot if possible
5. Commit with descriptive messages
6. Push to your fork
7. Open a Pull Request with:
   - Clear description of changes
   - Rationale for the update
   - Examples of improved behavior (if applicable)

## Review Criteria

PRs will be evaluated on:
- Clarity and usefulness of the context
- Accuracy of information
- Consistency with existing structure
- Quality of examples
- Overall improvement to AI assistance

## Code of Conduct

- Be respectful and constructive
- Focus on improving the project
- Welcome feedback and discussion
- Help others learn and grow

## Questions?

If you have questions about contributing:
- Open an issue for discussion
- Review existing documentation
- Check the [GitHub Copilot documentation](https://docs.github.com/copilot)

## Recognition

Contributors who improve the AI agent context will be acknowledged in:
- Git commit history
- PR comments and discussions
- Project documentation (if significant contributions)

## License

By contributing, you agree that your contributions will be licensed under the same license as this project (GPL-3.0).

---

Thank you for helping make this project more useful for AI-assisted development!
